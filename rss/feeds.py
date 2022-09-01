import contextlib
import pickle
from pathlib import Path
from typing import List, Optional

from graia.saya import Channel

from .model import RSSFeed

channel = Channel.current()

DATA_PATH = Path(__file__).parent / "data"
DATA_PATH.mkdir(exist_ok=True)
PICKLE_PATH = Path(DATA_PATH, "feeds.pickle")


def load_feeds() -> List[RSSFeed]:
    if PICKLE_PATH.is_file():
        with PICKLE_PATH.open("rb") as f:
            return pickle.load(f)
    save_pickle([])
    return []


def save_pickle(_feeds: List[RSSFeed]):
    with PICKLE_PATH.open("wb") as f:
        pickle.dump(_feeds, f)


feeds: List[RSSFeed] = load_feeds()


def register_feed(
    title: str,
    description: str,
    url: str,
    *,
    group: Optional[int] = None,
    friend: Optional[int] = None,
):
    if not title or not description or not url:
        raise ValueError("title, description and url cannot be None")
    if group is None and friend is None:
        raise ValueError("group and friend cannot be None at the same time")
    if feed := filter_feed(url):
        if group is not None:
            feed.groups.add(group)
        if friend is not None:
            feed.friends.add(friend)
    else:
        feed = RSSFeed(
            title=f"{title}:{description}",
            url=url,
            groups=[group] if group is not None else [],
            friends=[friend] if friend is not None else [],
        )
        feeds.append(feed)
    save_pickle(feeds)


def unregister_feed(url: str, group: Optional[int] = None, friend: Optional[int] = None):
    if group is None and friend is None:
        raise ValueError("group and friend cannot be None at the same time")
    with contextlib.suppress(ValueError):
        if feed := filter_feed(url):
            if group is not None:
                feed.groups.remove(group)
            if friend is not None:
                feed.friends.remove(friend)
            if not feed.groups and not feed.friends:
                feeds.remove(feed)
        save_pickle(feeds)


def filter_feed(url: str) -> RSSFeed:
    return next(filter(lambda x: x.url == url, feeds), None)


def remove_feed(title: str, description: str = None):
    global feeds
    with contextlib.suppress(ValueError):
        if description:
            feeds = list(filter(lambda x: x.title != f"{title}:{description}", feeds))
        else:
            feeds = list(filter(lambda x: not x.title.startswith(f"{title}:"), feeds))
        save_pickle(feeds)


def get_feed_from_id(group: Optional[int] = None, friend: Optional[int] = None):
    if group is None and friend is None:
        raise ValueError("group and friend cannot be None at the same time")
    if group is not None:
        return list(filter(lambda x: group in x.groups, feeds))
    return list(filter(lambda x: friend in x.friends, feeds))

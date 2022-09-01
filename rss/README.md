# RSS

## 使用方法

### 安装

1. 直接将该文件夹复制至 `modules` 文件夹下

2. 根据 `requirements.txt` 安装依赖 `feedparser`

3. 修改 `sagiri_bot.orm.async_orm`，修改内容如下

    ```python
    # 引入 TEXT
   from sqlalchemy import TEXT
   
   # 在文件末尾添加
   class RSSFeedTable(Base):
       """RSS Feed"""

       __tablename__ = "rss_feed"

       feed_id = Column(Integer, primary_key=True)
       title = Column(TEXT, nullable=False)
       summary = Column(TEXT, nullable=False)
       published = Column(DateTime, nullable=False)
       id = Column(TEXT, nullable=False)
       link = Column(TEXT, nullable=False)
       author = Column(TEXT, nullable=False)
       feed = Column(TEXT, nullable=False)
    ```

4. 按提示修改 `config.py`

5. 使用 `SayaManager` 或重启加载插件

### 注册/取消注册 RSS Feed

```python
# 以 https://example.com/rss 为例

from modules.rss.feeds import register_feed, unregister_feed

# 注册
register_feed(
   title="Example",
   description="Example RSS Feed",
   url="https://example.com/rss",
   group=114514,
   friend=None,
)

# 取消注册
unregister_feed(
   url="https://example.com/rss",
   group=114514,
   friend=None,
)
```

### 编写监听 RSS 更新的插件

该插件提供可监听的 `RSSUpdate` 事件，同时提供了 `FeedFileter` 修饰器以快速筛选 `RSSUpdate` 事件

```python
channel = Channel.current()

@channel.use(
    ListenerSchema(
        listening_events=[RSSUpdate],
        decorators=[FeedFilter.check("Twitter")]
    )
)
async def on_update(
    app: Ariane, 
    event: RSSUpdate,
    feed: RSSFeed,
    items: RSSFeedItems,
): ...
```

## 使用须知

1. 本插件仅对于 `MySQL` 作出优化，且仅能保证在 `MySQL` 下正常运行

2. 本插件暂未经过严格测试，可能存在未知的 Bug

3. 已注册的 RSS Feed 会在 `modules/rss/data` 中以 `pickle` 保存，如人为更改可能导致插件无法正常运行

| 插件名 |       作者       |     功能描述     | 注意事项                                                   | 是否耦合            |
|:---:|:--------------:|:------------:|:-------------------------------------------------------|:----------------|
| RSS | nullqwertyuiop | 为插件提供 RSS 功能 | 1. 该插件仅为依赖，不提供用户交互功能<br>2. 该插件**必须**安装在 `modules` 文件夹下 | 是（GlobalConfig） |

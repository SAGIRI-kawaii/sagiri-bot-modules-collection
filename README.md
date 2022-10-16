# sagiri-bot-modules-collection
适用于SAGIRI-BOT的第三方插件集合

这是一个存储基于 [Graia-Saya](https://github.com/GraiaProject/Saya) 并适用于 [SAGIRI-BOT](https://github.com/SAGIRI-kawaii/sagiri-bot) 的插件的仓库

如果您有这类项目，欢迎提交 Pull request 将您的项目添加到这里(注意，本仓库仅接受开源项目的仓库地址)

```diff
注意：本仓库仅提供插件存储，对插件内容并没有具体审查，请自行甄别
```

## 如何使用

按照插件的说明进行安装并重启机器人即可

## 插件列表

|   插件名   |       作者        |            功能描述             | 注意事项                                                   | 是否耦合            |
|:-------:|:---------------:|:---------------------------:|:-------------------------------------------------------|:----------------|
| B 站链接解析 | nullqwertyuiop  | 发送 B 站链接（包括 b23 短链）自动解析对应内容 | 含有多条链接时仅取第一条链接                                         | 是（Depend）       |
|  RSS    | nullqwertyuiop  |        为插件提供 RSS 功能         | 1. 该插件仅为依赖，不提供用户交互功能<br>2. 该插件**必须**安装在 `modules` 文件夹下 | 是（GlobalConfig） |


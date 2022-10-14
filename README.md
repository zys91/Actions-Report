# Actions_Report

## 食用指北

1. 先 Fork 到自己仓库，建议选择 Public 仓库，Private 仓库的 Action 功能有使用时长限制
2. 进入自己的仓库页面
3. 首次使用 Github Action 功能，先去 Action 页面启用
4. 进入 Settings 页面，找到 Secrets 栏目，选择 Actions，点击 New repository secret，Name 和 Value 填写看下方账号配置说明
5. 默认定时每天早上 7:30 打卡，可自行在 .github/workflows/Actions-Report.yml 文件中修改
6. 打卡内容默认和上一次打卡内容保持一致
7. 支持 Server酱、Bark、Telegram、企业微信等多种方式推送消息，若要启用此功能，参考下方通知配置说明
8. 仓库如果处于非活动状态达60天，Github Action计划的工作流将会自动禁用，所以需要定期手动启用相应工作流

Action Secrets 说明：

账号配置说明：（必选）

```JSON
Name：
SEU_REPORT_INFORM
Value：
{
  "seu_account": {
    "username": "一卡通号", 
    "password": "信息门户密码", 
    "name": "姓名"
  }
}
```

通知配置说明：（可选）

```markdown
## 通知环境变量，根据需求自行在 Github Action Secrets 中配置相关变量
## 变量格式说明：export Name="Value"

## 1. Server酱
## https://sct.ftqq.com
## 下方填写 SCHKEY 值或 SendKey 值
export SCKEY=""

## 2. BARK
## 下方填写app提供的设备码，例如：https://api.day.app/123 那么此处的设备码就是123
# bark服务,自行搜索
export BARK=""
# bark自建服务器，要填完整链接，结尾的/不要
export BARK_PUSH=""

## 3. Telegram
## 下方填写自己申请@BotFather的Token，如10xxx4:AAFcqxxxxgER5uw
export TG_BOT_TOKEN=""
## 下方填写 @getuseridbot 中获取到的纯数字ID
export TG_USER_ID=""
## Telegram 代理IP（选填）
## 下方填写代理IP地址，代理类型为 http，比如您代理是 http://127.0.0.1:1080，则填写 "127.0.0.1"
export TG_PROXY_IP=""
## Telegram 代理端口（选填）
## 下方填写代理端口号，代理类型为 http，比如您代理是 http://127.0.0.1:1080，则填写 "1080"
export TG_PROXY_PORT=""
## Telegram api自建反向代理地址（选填）
## 教程：https://www.hostloc.com/thread-805441-1-1.html
## 如反向代理地址 http://aaa.bbb.ccc 则填写 aaa.bbb.ccc
## 如需使用，请赋值代理地址链接
export TG_API_HOST=""

## 4. 钉钉
## 官方文档：https://developers.dingtalk.com/document/app/custom-robot-access
## 下方填写token后面的内容，只需 https://oapi.dingtalk.com/robot/send?access_token=XXX 等于=符号后面的XXX即可
export DD_BOT_ACCESS_TOKEN=""
export DD_BOT_SECRET=""

## 5. QQ
# qq机器人的QQ_SKEY
export QQ_SKEY=""
# qq机器人的QQ_MODE
export QQ_MODE=""

## 6. 企业微信机器人
## 官方说明文档：https://work.weixin.qq.com/api/doc/90000/90136/91770
## 下方填写密钥，企业微信推送 webhook 后面的 key
export QYWX_KEY=""

## 7. 企业微信应用
## 参考文档：http://note.youdao.com/s/HMiudGkb
## 下方填写素材库图片id（corpid,corpsecret,touser,agentid），素材库图片填0为图文消息, 填1为纯文本消息
export QYWX_AM=""

## 8. 微信推送Plus+
## 参考文档：http://pushplus.hxtrip.com/
export PUSH_PLUS_TOKEN=""
```

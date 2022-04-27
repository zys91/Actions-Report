# Actions_Report

## 食用指北

1. 先 Fork 到自己仓库，建议选择 Public 仓库，Private 仓库的 Action 功能有使用时长限制
2. 进入自己的仓库页面
3. 首次使用 Github Action 功能，先去 Action 页面启用
4. 进入 Settings 页面，找到 Secrets 栏目，选择 Actions，点击 New repository secret，Name 和 Value 填写看最下面说明
5. 点击 Star 收藏按钮可以手动触发一次打卡（你自己点击才有效，其他人点击无效）
6. 默认定时每天早上 7:30 打卡，可自行在 .github/workflows/Actions-Report.yml 文件中修改
7. 打卡内容默认和上一次打卡内容保持一致
7. 支持 [Server酱](https://sct.ftqq.com/) 微信推送，若要启用此功能，自行注册并在 serverchan 中填写推送KEY，若不启用，则留空

Action Secrets 说明：

Name：
```JSON
SEU_REPORT_INFORM
```
Value：

```JSON
{
  "seu_account": {
    "username": "一卡通号", 
    "password": "信息门户密码", 
    "name": "姓名"
  }, 
  "serverchan": "Server酱微信推送KEY/若不启用则留空"
}
```
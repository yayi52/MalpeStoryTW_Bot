角色情報站 MapleStory Discord Bot
===============================

簡介
----
「角色情報站」是一個 MapleStorySEA 角色資料追蹤工具。
主要功能：
1. 查詢角色資訊（等級、職業、伺服器、角色頭像）
2. 升級/裝備變化自動通知 Discord 頻道
3. 可視化角色資訊，方便玩家掌握進度

技術特色
---------
- Python 3
- Discord Bot（discord.py）
- 使用 MapleStory OpenAPI 抓取角色資料
- JSON 資料處理，可擴展排行榜、分析等功能

環境設定
----------
1. 安裝 Python 3
2. 安裝必要套件
3. 設定config.ini：
- TOKEN=<你的Bot Token>
- CHANNEL_ID=<要發送訊息的頻道ID>
- API_KEY=<你的MapleStory API Key>

使用方法
----------
1. 將 Bot 邀請到 Discord 伺服器（確保勾選 `bot` 和 `applications.commands` 權限）
2. 執行程式
3. 在 Discord 頻道使用 Slash 指令
4. Bot 會回傳角色資訊（等級、職業、伺服器、頭像等）

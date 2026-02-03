# 💼 台灣徵才活動助手 (mcp-tw-job-fair)

這是一個 Model Context Protocol (MCP) 伺服器，旨在提供台灣各地的徵才活動資訊。

## 🛠️ 安裝 (Installation)

1. 建立虛擬環境並安裝依賴：
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 🚀 配置 (Configuration)

### 🛠 Dive Configuration
- **Type**: `stdio`
- **Command**: `/Users/simonliuyuwei/clawd/projects/mcp-tw-job-fair/.venv/bin/python`
- **Args**: `/Users/simonliuyuwei/clawd/projects/mcp-tw-job-fair/src/server.py`

### 🛠 Claude Desktop Configuration
```json
{
  "mcpServers": {
    "mcp-tw-job-fair": {
      "command": "/Users/simonliuyuwei/clawd/projects/mcp-tw-job-fair/.venv/bin/python",
      "args": ["/Users/simonliuyuwei/clawd/projects/mcp-tw-job-fair/src/server.py"]
    }
  }
}
```

import requests
from bs4 import BeautifulSoup
import sys

def fetch_job_fairs():
    """
    從勞動力發展署或相關公開資訊抓取徵才活動資訊 (模擬邏輯)。
    """
    try:
        # 實際開發時應使用官方 API 或穩定網址
        # 這裡模擬回傳資料
        data = [
            {"date": "2026-02-10", "location": "台北車站", "title": "2026 科技業聯合徵才"},
            {"date": "2026-02-15", "location": "台中市政府", "title": "中部地區聯合就業博覽會"},
            {"date": "2026-02-20", "location": "高雄展覽館", "title": "南台灣薪資起飛徵才日"}
        ]
        return data
    except Exception as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
        return []

def filter_fairs_by_region(region):
    fairs = fetch_job_fairs()
    return [f for f in fairs if region in f['location']]

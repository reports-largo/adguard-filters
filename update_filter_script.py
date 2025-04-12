import requests
from datetime import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Referer': 'https://280blocker.net/'
}

now = datetime.now()
year = now.year
month = now.month

current_filename = f"280blocker_adblock_{year:04d}{month:02d}.txt"
base_url = "https://280blocker.net/files/"
current_url = base_url + current_filename
output_filename = "280blocker_adblock.txt" # 保存するファイル名は固定

response = requests.get(current_url, headers=headers)

if response.status_code == 200:
    # ... (以降の処理は同じ)
else:
    print(f"Error: 当月 ({current_filename}) のフィルターリストが見つかりませんでした (Status Code: {response.status_code})")
    exit(1)

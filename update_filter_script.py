import requests
from datetime import datetime

now = datetime.now()
year = now.year
month = now.month

current_filename = f"280blocker_adblock_{year:04d}{month:02d}.txt"
base_url = "https://280blocker.net/files/"
current_url = base_url + current_filename
output_filename = "280blocker_adblock.txt" # 保存するファイル名は固定

response = requests.get(current_url)

if response.status_code == 200:
    # ファイルが存在する場合
    filter_content = response.text
    with open(output_filename, "w") as f:
        f.write(filter_content)
    print(f"Successfully downloaded and saved: {current_filename}")
else:
    print(f"Error: 当月 ({current_filename}) のフィルターリストが見つかりませんでした (Status Code: {response.status_code})")
    exit(1)

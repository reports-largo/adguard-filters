from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

# Firefox をヘッドレスモードで起動
options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)

try:
    # 280blocker にアクセス
    driver.get("https://280blocker.net/files/280blocker_adblock.txt")
    time.sleep(2)  # サーバー応答待ち

    # フィルター内容を取得
    filter_content = driver.find_element("tag name", "pre").text

    # ファイルに保存
    with open("280blocker_adblock.txt", "w", encoding="utf-8") as f:
        f.write(filter_content)

    print("Successfully downloaded 280blocker filter")
finally:
    driver.quit()

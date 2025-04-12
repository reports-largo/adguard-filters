name: Auto Update 280blocker Filter

on:
  schedule:
    - cron: '0 15 * * *' # 毎日午前0時に実行 (JSTだと午前9時)
  workflow_dispatch: # 手動実行を可能にする

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          pip install requests
          pip install selenium  # selenium をインストールするコマンドを追加

      - name: Set User-Agent
        run: echo "USER_AGENT=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" >> $GITHUB_ENV

      - name: Download and update filter
        run: python update_filter_script.py
          env:
            USER_AGENT: ${{ env.USER_AGENT }}

      - name: Commit and push changes
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          git config --global user.name "Your Bot Name"
          git config --global user.email "your-bot-email@example.com"
          git add 280blocker_adblock.txt # 保存したファイル名
          if git diff --staged --quiet; then
            echo "No changes to commit."
          else
            git commit -m "自動更新: 280blockerフィルターを更新"
            git push origin main
          fi

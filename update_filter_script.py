name: Update 280blocker filter

on:
  schedule:
    - cron: '0 0 * * *'  # 毎日 9:00 JST
  workflow_dispatch:

jobs:
  update-280blocker:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Download latest 280blocker filter
        run: curl -L -o filters/280blocker.txt https://280blocker.net/files/280blocker_adblock.txt

      - name: Commit and push changes
        run: |
          git config --global user.name 'GitHub Actions'
          git config --global user.email 'actions@github.com'
          git add filters/280blocker.txt
          git commit -m 'Auto-update 280blocker filter' || echo "No changes to commit"
          git push

const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {
  // ヘッドレスモードをfalseに設定
  const browser = await puppeteer.launch({
    headless: false, // ヘッドレスモードを無効化
    args: [
      '--no-sandbox', 
      '--disable-setuid-sandbox', 
      '--disable-gpu', 
      '--window-size=1280x1024', 
      '--ignore-certificate-errors',
    ]
  });

  const page = await browser.newPage();

  // 280blocker のフィルターURL
  const url = 'https://280blocker.net/files/280blocker_adblock_202504.txt';

  // ページにアクセス
  await page.goto(url, { waitUntil: 'networkidle0' });

  // コンテンツを取得して保存
  const content = await page.content();

  // フォルダが無ければ作成
  fs.mkdirSync('filters', { recursive: true });

  // 取得したコンテンツ（フィルター）を保存
  fs.writeFileSync('filters/280blocker.txt', content);

  console.log('✅ Successfully downloaded and saved 280blocker filter');

  // ブラウザを閉じる
  await browser.close();
})();

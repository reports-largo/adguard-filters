const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {
  const browser = await puppeteer.launch({
    headless: true, // ヘッドレスモード
    args: ['--no-sandbox', '--disable-setuid-sandbox'] // セキュリティ周りの設定
  });
  const page = await browser.newPage();

  const url = 'https://280blocker.net/files/280blocker_adblock_202504.txt';

  // ページにアクセス
  await page.goto(url, { waitUntil: 'networkidle0' });

  // コンテンツを取得して保存
  const content = await page.content();
  
  // フォルダが無い場合は作成
  fs.mkdirSync('filters', { recursive: true });

  // 取得したコンテンツ（フィルター）を保存
  fs.writeFileSync('filters/280blocker.txt', content);

  console.log('✅ Successfully downloaded and saved 280blocker filter');

  await browser.close();
})();

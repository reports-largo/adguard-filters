const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {
  const browser = await puppeteer.launch({
    headless: false, // GitHub Actions 環境ではXvfbを使ってGUIエミュレート
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-gpu',
      '--window-size=1280x1024',
      '--ignore-certificate-errors',
    ]
  });

  const page = await browser.newPage();

  const url = 'https://280blocker.net/files/280blocker_adblock_202504.txt';

  try {
    await page.goto(url, { waitUntil: 'networkidle0' });
    const content = await page.content();

    // フォルダ作成
    fs.mkdirSync('../filters', { recursive: true });

    // Cloudflare ブロックチェック
    if (content.includes('Cloudflare') || content.includes('Sorry, you have been blocked')) {
      console.error('⚠️ Cloudflare block detected. Skipping update.');
    } else {
      fs.writeFileSync('../filters/280blocker.txt', content);
      console.log('✅ Successfully downloaded and saved 280blocker filter');
    }

  } catch (error) {
    console.error('❌ Error downloading filter:', error);
  }

  await browser.close();
})();
const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {
  const browser = await puppeteer.launch({
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
    const content = await page.evaluate(() => {
      return document.body.innerText;
    });

    fs.mkdirSync('filters', { recursive: true });
    fs.writeFileSync('filters/280blocker.txt', content);

    console.log('✅ Successfully downloaded and saved 280blocker filter');

  } catch (error) {
    console.error('Error during download or save:', error);
  } finally {
    await browser.close();
  }
})();

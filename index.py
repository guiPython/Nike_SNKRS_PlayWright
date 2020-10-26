import asyncio
from playwright import async_playwright
import os.path
from login import login

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(executablePath="C:\Program Files\Google\Chrome\Application\chrome.exe", headless=False)
        page = await browser.newPage()
        page.setDefaultTimeout(0)
        access = await asyncio.wait([login(page,'','')])
        if access:
            return True
        await browser.close()
    return True

asyncio.get_event_loop().run_until_complete(main())

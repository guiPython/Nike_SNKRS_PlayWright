from playwright import async_playwright
from dotenv import load_dotenv
from pathlib import Path
from login import login
import asyncio
import os


load_dotenv()

async def main():
    email = os.getenv("EMAIL")
    senha = os.getenv("SENHA")
    async with async_playwright() as p:
        browser = await p.chromium.launch(executablePath="C:\Program Files\Google\Chrome\Application\chrome.exe", headless = False)
        page = await browser.newPage()
        page.setDefaultTimeout(0)
        access = await asyncio.wait([login(browser,page,email,senha)])
        if access:
            input()
            await browser.close()
            return True
    return True

asyncio.get_event_loop().run_until_complete(main())

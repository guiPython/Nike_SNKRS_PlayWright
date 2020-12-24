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
        browser = await p.webkit.launch(headless=False)
        page = await browser.newPage()
        page.setDefaultTimeout(0)

        access = asyncio.create_task(login(browser,page,email,senha))
        done , pending = await asyncio.wait({access},return_when="ALL_COMPLETED")
        
        if access in done :
            print("Login: Success")
            await browser.close()
            return True
        else:
            print("Login: Failed")
            await browser.close()
    return True

asyncio.get_event_loop().run_until_complete(main())

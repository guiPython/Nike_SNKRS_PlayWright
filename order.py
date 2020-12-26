import asyncio
from playwright import async_playwright , TimeoutError

async def order(browser , page , size: str):
    await page.click()
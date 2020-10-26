import asyncio
from playwright import async_playwright

async def login(page , emailUser: str , senhaUser: str) -> bool:
    await page.goto("https://www.nike.com.br/Snkrs",waitUntil='load')
    await page.click("#anchor-acessar")
    await page.waitForTimeout(700)
    await page.type('input[name="emailAddress"]',emailUser,delay=150)
    await page.waitForTimeout(500)
    await page.type('input[name="password"',senhaUser,delay=150)
    await page.waitForTimeout(500)
    await page.keyboard.press('Enter')
    await page.waitForNavigation(waitUntil='load')
    return True
import asyncio
from playwright import async_playwright

async def login(browser , page , emailUser: str , senhaUser: str) -> bool:
    await page.goto("https://www.nike.com.br/Snkrs",waitUntil='load')
    await page.click("#anchor-acessar")
    await page.waitForTimeout(700)
    if emailUser and senhaUser != "":
        await page.type('input[name="emailAddress"]',emailUser,delay=150)
        await page.waitForTimeout(500)
        await page.type('input[name="password"',senhaUser,delay=150)
        await page.waitForTimeout(500)
        await page.keyboard.press('Enter')
        await page.waitForNavigation(waitUntil='load')
        return True
    else:
        await browser.close()
        print("Insira um email e/ou senha validos.")
        return False
    
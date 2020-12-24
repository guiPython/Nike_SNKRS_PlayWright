import asyncio
from playwright import async_playwright

async def login(browser , page , emailUser: str , senhaUser: str) -> bool:
    await page.goto("https://www.nike.com.br",waitUntil='load')
    await page.click("#anchor-acessar")
    await page.waitForTimeout(700)
    if emailUser and senhaUser != "":
        try:
            await page.type('input[name="emailAddress"]',emailUser,delay=250)
            await page.waitForTimeout(2000)
            await page.type('input[name="password"',senhaUser,delay=250)
            await page.waitForTimeout(1000)
            await page.click('#keepMeLoggedIn')
            await page.waitForTimeout(5000)
            await page.click('input[value="ENTRAR"')
            await page.waitForNavigation(waitUntil='load')
            return True
        except TimeoutError:
            return False
    else:
        await browser.close()
        print("Insira um email e/ou senha validos.")
        return False
    
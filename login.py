import asyncio
from playwright import async_playwright , TimeoutError 


async def login(browser , page , emailUser: str , senhaUser: str , product: str):
    await page.goto(f"https://www.nike.com.br/Snkrs/Produto/{product}",waitUntil='load')
    await page.click("#anchor-acessar")
    await page.waitForTimeout(1000)
    if emailUser and senhaUser != "":
        try:
            await page.type('input[name="emailAddress"]',emailUser,delay=150)
            await page.waitForTimeout(2000)
            await page.type('input[name="password"]',senhaUser,delay=250)
            await page.waitForTimeout(1000)
            await page.click('#keepMeLoggedIn')
            await page.waitForTimeout(5000)
            await page.click('input[value="ENTRAR"]')
            await page.waitForNavigation(waitUntil='networkidle',timeout=30000)
            await page.waitForXPath('//*[@id="header"]/div[1]/div/div/div[2]/span[1]/span[1]/span/a')
            return { 'mensagem' : "LOGIN : SUCCESS" , 'status' : True } 
        except TimeoutError:
            await browser.close()
            return { 'mensagem' : "LOGIN : FAILED" , 'status' : False }
    else:
        await browser.close()
        print("Insira um email e/ou senha validos.")
        return { 'mensagem' : "LOGIN : FAILED" , 'status' : False }
    
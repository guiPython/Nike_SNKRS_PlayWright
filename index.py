from playwright import async_playwright
from dotenv import load_dotenv
from pathlib import Path
from login import login
#from order import order
#from pay import pay
import asyncio
import os


load_dotenv()

async def main():
    email = os.getenv("EMAIL")
    senha = os.getenv("SENHA")
    produto = os.getenv("PRODUTO")
    async with async_playwright() as p:

        browser = await p.firefox.launch(headless=False)
        page = await browser.newPage()
        page.setDefaultTimeout(0)

        access =  asyncio.create_task(login(browser,page,email,senha,produto))
        #order  =  asyncio.create_task(order(browser,page,email,senha))
        #pay    =  asyncio.create_task(pay(browser,page,email,senha))
        tasks = [ access ]

        for task in tasks:
            done ,  pending =  await asyncio.wait({task},return_when="FIRST_EXCEPTION")
            if task in done:
                resultado = task.result()
                if not resultado['status']:
                    print( resultado['mensagem'] )
                    break

asyncio.get_event_loop().run_until_complete(main())

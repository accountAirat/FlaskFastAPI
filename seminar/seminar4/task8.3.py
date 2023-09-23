import asyncio
from pywebcopy import save_website
import time

tasks = []
start_time = time.time()
urls = ['https://megaseller.shop/', ]


async def website(url, folder='./'):
    name = 'async_' + url.replace('https://', '').replace('.', '_').replace('/', '')
    save_website(
        url=url,
        project_folder=folder,
        project_name=name,
        bypass_robots=True,
        debug=True,
        delay=None,
    )
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


async def main():
    for url in urls:
        task = asyncio.ensure_future(website(url))
        tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())

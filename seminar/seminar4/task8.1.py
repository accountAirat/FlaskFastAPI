from pywebcopy import save_website
import threading
import time

threads = []
start_time = time.time()
urls = ['https://megaseller.shop/', ]


def website(url, folder='./'):
    name = 'thread_' + url.replace('https://', '').replace('.', '_').replace('/', '')
    save_website(
    url=url,
    project_folder=folder,
    project_name=name,
    bypass_robots=True,
    debug=True,
    delay=None,
    )
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


for url in urls:
    thread = threading.Thread(target=website, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
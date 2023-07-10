import asyncio
import aiohttp
from get_url import get_all_website_links
from datetime import datetime


async def download(url):
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as response:
			text = await response.text()
			filename = 'data\\async_' + url.replace('https:', '').replace('/', '').replace('.', '_') + ".html"
			with open(filename, 'w', encoding='utf8') as f:
				f.write(text)


async def main():
	import argparse
	
	parser = argparse.ArgumentParser(description="Этот скрипт загружает все изображения с веб‑страницы.")
	parser.add_argument("url", help="URL‑адрес веб‑страницы, с которой вы хотите загрузить изображения.")
	args = parser.parse_args()
	url = args.url
	urls = get_all_website_links(url)
	print(urls)
	dt = datetime.now()
	tasks = []
	
	for url in urls:
		task = asyncio.ensure_future(download(url))
		tasks.append(task)
	await asyncio.gather(*tasks)
	
	print(f'Общее время загрузки {datetime.now() - dt}')


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())


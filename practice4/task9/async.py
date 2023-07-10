import asyncio
from datetime import datetime
import os
import aiohttp
from get_url import get_all_images


async def download(url):
	"""Сохраняем полученные изображения"""
	dti = datetime.now()
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as response:
			filename = os.path.join('data', 'async_' + url.split("/")[-1])
			with open(filename, 'wb') as f:
				async for chunk in response.content.iter_chunked(1024):
					f.write(chunk)
				print(f'Загружено изображение {filename} за  {datetime.now() - dti}')


async def main():
	import argparse
	
	parser = argparse.ArgumentParser(description="Этот скрипт загружает все изображения с веб‑страницы.")
	parser.add_argument("url", help="URL‑адрес веб‑страницы, с которой вы хотите загрузить изображения.")
	args = parser.parse_args()
	url = args.url
	imgs = get_all_images(url)
	dt = datetime.now()
	tasks = []
	
	for img in imgs:
		task = asyncio.ensure_future(download(img))
		tasks.append(task)
	await asyncio.gather(*tasks)
	
	print(f'Общее время загрузки {datetime.now() - dt}')


if __name__ == '__main__':
	asyncio.run(main())

from datetime import datetime
import os
import threading
import requests
from get_url import get_all_images


def save(url):
	"""Сохраняем полученные изображения"""
	response = requests.get(url)
	filename = os.path.join('data', 'thread_'+url.split("/")[-1])
	with open(filename, "wb") as f:
		f.write(response.content)
		print(f'Загружено избражение {filename} за  {datetime.now() - dt}')


if __name__ == "__main__":
	import argparse
	
	parser = argparse.ArgumentParser(description="Этот скрипт загружает все изображения с веб‑страницы.")
	parser.add_argument("url", help="URL‑адрес веб‑страницы, с которой вы хотите загрузить изображения.")
	args = parser.parse_args()
	url = args.url
	imgs = get_all_images(url)
	dt = datetime.now()
	threads = []
	
	for img in imgs:
		thread = threading.Thread(target=save, args=[img])
		threads.append(thread)
		thread.start()
	
	for thread in threads:
		thread.join()
		
	print(f'Общее время загрузки {datetime.now() - dt}')

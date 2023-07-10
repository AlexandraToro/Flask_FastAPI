from datetime import datetime
import os
import multiprocessing
import requests
from get_url import get_all_images



def save(url):
	"""Сохраняем полученные изображения"""
	response = requests.get(url)
	dti = datetime.now()
	filename = os.path.join('data', 'processing_' + url.split("/")[-1])
	with open(filename, "wb") as f:
		f.write(response.content)
		print(f'Загружено изображение {filename} за  {datetime.now() - dti}')


if __name__ == "__main__":
	import argparse
	
	parser = argparse.ArgumentParser(description="Этот скрипт загружает все изображения с веб‑страницы.")
	parser.add_argument("url", help="URL‑адрес веб‑страницы, с которой вы хотите загрузить изображения.")
	args = parser.parse_args()
	url = args.url
	imgs = get_all_images(url)
	dt = datetime.now()
	processes = []
	
	for img in imgs:
		process = multiprocessing.Process(target=save, args=(img,))
		processes.append(process)
		process.start()
	
	for process in processes:
		process.join()
	
	print(f'Общее время загрузки {datetime.now() - dt}')

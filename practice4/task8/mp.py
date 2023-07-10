import multiprocessing
import requests
from get_url import get_all_website_links
from datetime import datetime


def download(url):
	response = requests.get(url)
	filename = 'data\\multiprocessing_' + url.replace('https:', '').replace('/', '').replace('.', '_') + ".html"
	with open(filename, 'w', encoding='utf8') as f:
		f.write(response.text)


processes = []

if __name__ == '__main__':
	import argparse
	
	parser = argparse.ArgumentParser(description="Инструмент получения ссылок на web-странице")
	parser.add_argument("url", help="URL, по которому надо получить все ссылки")
	
	args = parser.parse_args()
	url = args.url
	urls = get_all_website_links(url)
	dt = datetime.now()
	for url in urls:
		process = multiprocessing.Process(target=download, args=(url,))
		processes.append(process)
		process.start()
	
	for process in processes:
		process.join()
	print(f'Время загрузки {datetime.now() - dt}')
	
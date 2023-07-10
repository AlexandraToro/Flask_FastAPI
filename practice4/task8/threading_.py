import threading
import requests
from get_url import get_all_website_links
from datetime import datetime


def download(url):
	response = requests.get(url)
	filename = 'data\\threading_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
	with open(filename, "w", encoding='utf-8') as f:
		f.write(response.text)


if __name__ == '__main__':
	import argparse
	
	parser = argparse.ArgumentParser(description="Инструмент получения ссылок на web-странице")
	parser.add_argument("url", help="URL, по которому надо получить все ссылки")
	
	args = parser.parse_args()
	url = args.url
	urls = get_all_website_links(url)
	print(urls)
	threads = []
	dt = datetime.now()
	for url in urls:
		thread = threading.Thread(target=download, args=[url])
		threads.append(thread)
		thread.start()
	
	for thread in threads:
		thread.join()
	
	print(f'Время загрузки {datetime.now() - dt}')

import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup


def is_valid(url):
	"""
	Проверяет, является ли url действительным URL
	"""
	parsed = urlparse(url)
	return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_website_links(url):
	"""
	Возвращает все URL-адреса, найденные на `url`, в котором он принадлежит тому же веб-сайту.
	"""
	# все URL-адреса `url`
	urls = set()
	# доменное имя URL без протокола
	domain_name = urlparse(url).netloc
	soup = BeautifulSoup(requests.get(url).content, "html.parser")
	for a_tag in soup.findAll("a"):
		href = a_tag.attrs.get("href")
		if href == "" or href is None:
			# href пустой тег
			continue
		# присоединяемся к URL, если он относительный (не абсолютная ссылка)
		href = urljoin(url, href)
		parsed_href = urlparse(href)
		# удалить GET-параметры URL, фрагменты URL и т. д.
		href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
		if not is_valid(href):
			# недействительный URL
			continue
		if href in urls:
			# уже в наборе
			continue
		urls.add(href)
	return urls


if __name__ == "__main__":
	import argparse
	
	parser = argparse.ArgumentParser(description="Инструмент получения ссылок на web-странице")
	parser.add_argument("url", help="URL, по которому надо получить все ссылки")

	args = parser.parse_args()
	url = args.url
	print(get_all_website_links(url))
	
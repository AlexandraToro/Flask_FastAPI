import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin


def get_all_images(url):
	"""
	Возвращает все URL‑адреса изображений по одному `url`
	"""
	soup = bs(requests.get(url).content, "html.parser")
	urls = []
	for img in soup.find_all("img"):
		img_url = img.attrs.get("src")
		if not img_url:
			# если img не содержит атрибута src, просто пропускаем
			continue
		# сделаем URL абсолютным, присоединив имя домена к только что извлеченному URL
		img_url = urljoin(url, img_url)
		# удалим URL‑адреса типа '/hsts-pixel.gif?c=3.2.5'
		try:
			pos = img_url.index("?")
			img_url = img_url[:pos]
		except ValueError:
			pass
		urls.append(img_url)
	return urls

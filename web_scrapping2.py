from bs4 import BeautifulSoup
import requests

url="https://.com"
req=requests.get(url).text

soup=BeautifulSoup(req, 'lxml')

for article in soup.find_all('article'):
	# print(article.prettify())

	headline=article.h2.a.text
	print(headline)

	summary=article.find('div', class_='entry-content').p.text
	print(summary)

	vid_src=article.find('iframe', class_='youtube-player')['src']
	vid_id=vid_src.split('/')[4].split('?')[0]
	# print(vid_src)
	# print(vid_id)

	yt_link=f'https://youtube.com/watch?v={vid_id}'
	print(yt_link)
	
	print()
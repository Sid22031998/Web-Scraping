from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/global/in-en/p/pl?d=graphics+card"
req=requests.get(url).text
soup=BeautifulSoup(req, "html.parser")
# print(soup.h1)
containers=soup.find_all("div", class_="item-container")


filename="products.csv"
f=open(filename, "w")
headers="brand, product_name, shipping\n"
f.write(headers)

for container in containers:
	brand = container.div.div.a.img['title']
	product_name = container.find_all("a", class_="item-title")[0].text
	shipping_cost = container.find_all("li", class_="price-ship")[0].text.strip()
	# print(brand)
	# print(product_name)
	# print(shipping_cost)
	# print()
	f.write(brand + "," + product_name.replace(",", " ") + "," + shipping_cost + "\n")

f.close()
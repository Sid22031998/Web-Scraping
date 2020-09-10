from bs4 import BeautifulSoup
import requests

url = "https://www.snapdeal.com/search?keyword=keyboard%20mouse&santizedKeyword=&catId=&categoryId=0&suggested=true&vertical=p&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=ALL&url=&utmContent=&dealDetail=&sort=rlvncy"
req=requests.get(url).text
# print(req)
soup=BeautifulSoup(req, "html.parser")
containers=soup.find_all("div", class_="favDp")

filename="snapdeal_keyboard.csv"
f=open(filename, "w")
headers="Brand,Product_Name,Price\n"
f.write(headers)

for container in containers:
	title=container.find("picture").img['title'].replace(",", " ")
	price=container.find("span", class_="product-price").text.replace(",", "")
	brand=title.split(' ')[0]
	# print(brand)
	# print(title)
	# print(price)
	# print()
	f.write(brand + "," + title + "," + price + "\n")

f.close()
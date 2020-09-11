from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("chromedriver.exe")
driver.get('http://sentimentanalysis2.herokuapp.com/')

url="https://www.trustpilot.com/"
req=requests.get(url).text

soup=BeautifulSoup(req, 'html.parser')
reviews=soup.find_all("div", class_="reviewCard___2KiId")

for review in reviews:
	author=review.find("div", class_="author___3-7MA").a.text.strip()
	rev=review.find("div", class_="reviewCardBody___2o5Ws").text
	# print(author)
	# print(rev)
	search_bar = driver.find_element_by_xpath('/html/body/div/p[3]/textarea')
	search_bar.send_keys(Keys.CONTROL + "a")
	search_bar.send_keys(Keys.BACKSPACE)
	search_bar.send_keys(rev)
	button=driver.find_element_by_xpath('/html/body/div/p[4]/button')
	button.send_keys(Keys.ENTER)
	break
	print()


import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://www.eldorado.ru/") #сайт с которого парсить (главное не забыть / после названия, а то не будет работать)
print(r.status_code) #статус соединения
html = BS(r.content, "html.parser")

for el in html.select(".slick-slide"): #элементы которые парсить
	title = el.select(".zqgg6c-2 > a") #дочерние элементы
	price = el.select(".zqgg6c-7")
	
	try:
		print(title[0]["title"] + " " + price[0].text) #вывод контента до получения ошибки
	except IndexError:
		continue

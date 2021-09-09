import requests
from bs4 import BeautifulSoup as bs
site = "http://utmiit.ru/ZR/ZR1.htm"
content = requests.get(site)
soup = bs(content.text.encode("cp1252").decode("cp1251"), "html.parser")
group_name = input("Введите название группы: ")

for tr in soup.find_all("tr"):
	group = tr.find("td", class_="xl20")

	try:
		if group_name == group.text:
			all_info = [x for i, x in enumerate(tr.find_all('td')) if i != 0 and i != 1]

			print("Все предметы:\n\n{}".format("\n".join([f"{x+1}. {all_info[i].text} ({all_info[i+1].text})" if all_info[i].text != '\xa0' else f"{x+1}. Нету пары ()" for x, i in enumerate(range(0, 8, 2))])))
	except AttributeError:
		continue

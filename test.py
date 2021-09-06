import requests
from bs4 import BeautifulSoup as bs

content = requests.get("http://utmiit.ru/ZR/ZR1.htm")
soup = bs(content.text.encode("cp1252").decode('cp1251'), 'html.parser')
group_name = input("Введите название группы: ") ##Имя группы

for tr in soup.find_all("tr"):
	group = tr.find("td", class_="xl20")

	try:
		if group.text == group_name:
			print("Группа: {}\n".format(group.text))
			all_par = tr.find_all("td", class_="xl21")
			all_cab = tr.find_all("td", class_="xl22")

			for i, x in enumerate(all_par):
				print("{}. {} ({})".format(i+1, x.text.rstrip(), all_cab[i].text))
	except Exception:
		continue
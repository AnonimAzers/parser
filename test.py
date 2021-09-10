import requests
from bs4 import BeautifulSoup as bs

##Получение контента с сайта
site = "http://utmiit.ru/ZR/ZR1.htm"
content = requests.get(site)
soup = bs(content.text.encode("cp1252").decode("cp1251"), "html.parser")

##Регистрация команд
commands = ["/станадркабинет", "/расп", "/каб"]

class FinderInfo:
	default_group = None

	def get_schedule(group_name):
		for tr in soup.find_all("tr"):
			group = tr.find("td", class_="xl20")

			try:
				if group_name == group.text:
					all_info = [x for i, x in enumerate(tr.find_all('td')) if i != 0 and i != 1]

					print("Все предметы:\n\n{}".format("\n".join([f"{x+1}. {all_info[i].text} ({all_info[i+1].text})" if all_info[i].text != '\xa0' else f"{x+1}. Нету пары ()" for x, i in enumerate(range(0, 8, 2))])))
			except AttributeError:
				continue

	def get_les_in_office(office):
		print("Все пары, проходящие в этом кабинете сегодня: \n")
		index_content = 0	
		for tr in soup.find_all("tr"):
			content = tr.find_all("td")

			for i, block in enumerate(content):
				try:
					if block.attrs['class'][0] == "xl22" and block.text == office:
						index_content += 1
						print(f"{index_content}. {content[i-1].text}")
				except Exception:
					continue




if __name__ == "__main__":
	while True:
		command = [x for x in input("Введите команду: ").split()]

		if command[0] in commands:
			if command[0] == commands[0]:
				FinderInfo.default_group = input("Введите название группы, которая будет установлена по умолчанию: ")
				print(f"Установлена группа по умолчанию: {FinderInfo.default_group}")

			if command[0] == commands[1]:
				if len(command) == 1:
					if FinderInfo.default_group != None:
						FinderInfo.get_schedule(FinderInfo.default_group)
					else:
						print("Не установлена группа по умолчанию!")
				elif len(command) == 2:
					FinderInfo.get_schedule(command[1])
				else:
					print('Вы неверно ввели параметры команды!')

			if command[0] == commands[2]:
				if len(command) == 2:
					FinderInfo.get_les_in_office(command[1])
				else:
					print('Вы неверно ввели параметры команды!')
		else:
			print('Такой команды не существует!')

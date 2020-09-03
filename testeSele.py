from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

browser = webdriver.Firefox()

class UserBotInsta:
	def __init__(self,n_user,password,comentario):
		self.n_user = n_user
		self.password = password
		self.comentario = comentario

	def logar(self):
		browser.get('https://www.instagram.com/')
		time.sleep(2)
		
		name_button = browser.find_element_by_name("username")
		name_button.clear()
		name_button.send_keys(self.n_user)

		passw_button = browser.find_element_by_name("password")
		passw_button.clear()
		passw_button.send_keys(self.password)

		passw_button.send_keys(Keys.RETURN)
		time.sleep(3)

		self.divulgar()


	@staticmethod
	def digitarLento(comentario,area_digitar):
		for i in comentario:
			area_digitar.send_keys(i)



		


	def divulgar(self):
		browser.get("https://www.instagram.com/hilton_cn/")
		time.sleep(3)

		for i in range(1,2):
			browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
			time.sleep(3)

		hrefs = browser.find_elements_by_tag_name('a')
		hrefs_split = [elem.get_attribute('href') for elem in hrefs]

		#link das fotos
		hrefs_list = []

		#filtrando fotos
		for i in hrefs_split:  
			if "instagram.com/p/" in i:
				hrefs_list.append(i)

		for imagem in hrefs_list:
			browser.get(imagem)

			try:
				browser.find_element_by_class_name('Ypffh').click()
				comentario_barra = browser.find_element_by_class_name('Ypffh')
				self.digitarLento("isso eh um teste",comentario_barra)
				browser.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
				time.sleep(random(48,60))
				#time.sleep(random.randint(50))

			except Exception as e:
				time.sleep(3)

		



userBot = UserBotInsta("TheDivulgador21",
						"Divulgador8491",
						"Para você que tem interesse roupas sob medida, moda praia,fitness e lingerie, da uma olhada no nosso trabalho https://www.instagram.com/laje44/?hl=pt-br ")


userBot.logar()
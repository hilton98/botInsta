from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from random import *

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
			#time.sleep(random.randrange(1,3)/17)


	def divulgar(self):
		browser.get("https://www.instagram.com/explore/")
		time.sleep(3)

		for i in range(1,3):
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

		print(hrefs_list)
		print(len(hrefs_list))

		for imagem in hrefs_list:
			browser.get(imagem)

			try:
				browser.find_element_by_class_name('Ypffh').click()
				comentario_barra = browser.find_element_by_class_name('Ypffh')

				self.digitarLento(self.comentario[randrange(len(self.comentario)  ) ],comentario_barra)
				time.sleep(3)
				
				browser.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
				time.sleep(25)
				#time.sleep(random.randint(50))

			except Exception as e:
				time.sleep(3)
		


frases = ["Da uma chegada na minha loja @laje44 :)","Roupas sob medida na @laje44 :)","Visita minha loja e faça seu pedido @laje44","Moda fitness e praiana é aqui msm @laje44", "Confere minha loja virtual @laje44"] 



userBot = UserBotInsta("TheDivulgador21","Divulgador8491", frases ) 





userBot.logar()


'''
PADROES DE LINK

instagram.com/p/  							--- Postagem
https://www.instagram.com/direct/inbox/ 	--- Direct
https://www.instagram.com/sixbrandbrasil/ 	--- Pagina ou usuario
https://www.instagram.com/explore/			--- Explore

'''
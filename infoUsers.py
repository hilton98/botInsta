from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time


browser = webdriver.Firefox()

browser.get('https://www.instagram.com/')
time.sleep(2)
		
name_button = browser.find_element_by_name("username")
name_button.clear()
name_button.send_keys("TheDivulgador21")

passw_button = browser.find_element_by_name("password")
passw_button.clear()
passw_button.send_keys("Divulgador8491")
passw_button.send_keys(Keys.RETURN)
time.sleep(3)


#coletar posts do explore
browser.get("https://www.instagram.com/explore/")
time.sleep(3)

for i in range(1,3):
	browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
	time.sleep(3)

hrefs = browser.find_elements_by_tag_name('a')
hrefs_split = [elem.get_attribute('href') for elem in hrefs]

#postagens
lista_posts = []

for i in hrefs_split:  
	if "instagram.com/p/" in i:
		lista_posts.append(i)

#print(lista_posts)
#print(len(lista_posts) )

for imagem in lista_posts:
	browser.get(imagem)
	try:
		browser.find_element_by_class_name('Ypffh').click()
		comentario_barra = browser.find_element_by_class_name('Ypffh')
		self.digitarLento("da uma olhada @laje44 :)",comentario_barra)
		time.sleep(3)
		browser.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
		time.sleep(25)
		#time.sleep(random.randint(50))

	except Exception as e:
		time.sleep(3)



'''
PADROES DE LINK

instagram.com/p/  							--- Postagem
https://www.instagram.com/direct/inbox/ 	--- Direct
https://www.instagram.com/sixbrandbrasil/ 	--- Pagina ou usuario
https://www.instagram.com/explore/			--- Explore

'''
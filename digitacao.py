from random import *

'''
lista = ['https://www.instagram.com/moda_fitness_oficial/', 'https://www.instagram.com/luuramundo/', 'https://www.instagram.com/moda_fitness_oficial/', 'https://www.instagram.com/p/CFINw_yD5SQ/', 'https://www.instagram.com/sixbrandbrasil/', 'https://www.instagram.com/tallitasl/', 'https://www.instagram.com/sixbrandbrasil/', 'https://www.instagram.com/p/CFF1MiZjDGJ/', 'https://www.instagram.com/thayna_sousaa_/', 'https://www.instagram.com/nathalia_gomesdossantos/', 'https://www.instagram.com/p/CFF1MiZjDGJ/', 'https://www.instagram.com/sixbrandbrasil/', 'https://www.instagram.com/beatriz_castelo17/', 'https://www.instagram.com/sixbrandbrasil/', 'https://www.instagram.com/p/CFJ8BoiDZEQ/', 'https://www.instagram.com/raphael_soares_lima/', 'https://www.instagram.com/vivi_estefany/', 'https://www.instagram.com/raiss_abarbosa/', 'https://www.instagram.com/p/CFJ8BoiDZEQ/', 'https://www.instagram.com/sixbrandbrasil/', 'https://www.instagram.com/katarinefsf/', 'https://www.instagram.com/sixbrandbrasil/', 'https://www.instagram.com/p/CFHznWcj82Z/', 'https://www.instagram.com/___feminicestore/', 'https://www.instagram.com/gabiimell_/', 'https://www.instagram.com/p/CFHznWcj82Z/', 'https://www.instagram.com/sixbrandbrasil/', 'https://www.instagram.com/raphael_soares_lima/', 'https://www.instagram.com/sixbrandbrasil/', 'https://www.instagram.com/raphael_soares_lima/', 'https://www.instagram.com/wnatyoliveira/', 'https://www.instagram.com/p/CFKXHIEj6kA/', 'https://www.instagram.com/sixbrandbrasil/', 'https://www.instagram.com/dynnaralimaa_/', 'https://www.instagram.com/sixbrandbrasil/', 'https://www.instagram.com/p/CFKqYYvDjX8/', 'https://www.instagram.com/sixbrandbrasil/', 'https://www.instagram.com/marciohenriquees/', 'https://www.instagram.com/sixbrandbrasil/', 'https://www.instagram.com/p/CFDSR9mj4DS/', 'https://www.instagram.com/andersondouradoo_/', 'https://www.instagram.com/lu_araujo_23/', 'https://www.instagram.com/p/CFDSR9mj4DS/', 'https://www.instagram.com/sixbrandbrasil/', 'https://www.instagram.com/suyanna/', 'https://www.instagram.com/sixbrandbrasil/', 'https://www.instagram.com/p/CFFL9VLjgOe/', 'https://www.instagram.com/janaellyr/', 'https://www.instagram.com/raynara_severo/', 'https://www.instagram.com/p/CFFL9VLjgOe/', 'https://www.instagram.com/thedivulgador21/', 'https://www.instagram.com/thedivulgador21/', 'https://www.instagram.com/explore/people/', 'https://www.instagram.com/essenbymarias/', 'https://www.instagram.com/essenbymarias/', 'https://www.instagram.com/instagram/', 'https://www.instagram.com/nike/', 'https://www.instagram.com/nike/', 'https://www.instagram.com/gal_gadot/', 'https://www.instagram.com/gal_gadot/', 'https://www.instagram.com/devwindsor/', 'https://about.instagram.com/', 'https://help.instagram.com/', 'https://about.instagram.com/blog/', 'https://www.instagram.com/developer/', 'https://www.instagram.com/about/jobs/', 'https://www.instagram.com/legal/privacy/', 'https://www.instagram.com/legal/terms/', 'https://www.instagram.com/explore/locations/', 'https://www.instagram.com/directory/profiles/', 'https://www.instagram.com/directory/hashtags/', 'https://www.instagram.com/', 'https://www.instagram.com/', 'https://www.instagram.com/direct/inbox/', 'https://www.instagram.com/explore/', 'https://www.instagram.com/accounts/activity/']

lista_posts = []

for i in lista:  
	if "instagram.com/p/" in i:
		lista_posts.append(i)

print(lista_posts)

mensagem = "MODA FITNESS, PRAIA só na @laje44 , entre outras... Roupas sob medida!!"

for i in mensagem:
	print(i)
	time.sleep(random.randrange(1,3)/17)
'''


def geraFraseRandom(frases):
		return frases[randrange(len(frases))]




frases = ["Da uma chegada na minha loja @laje44 :)","Roupas sob medida na @laje44 :)","Visita minha loja e faça seu pedido @laje44","Moda fitness e praiana é aqui msm @laje44", "Confere minha loja virtual @laje44"] 


print(geraFraseRandom(frases))
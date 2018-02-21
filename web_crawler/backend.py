#
from bs4 import BeautifulSoup
import requests

response = requests.get('https://pt.wikipedia.org/wiki/Framework')

html = response.text

soup = BeautifulSoup(html, 'html.parser')

print(soup.find(id="mw-content-text").p.a.get('href'))

print(soup.p.find_all('a'))

print(soup.p)

print(soup.p.a)

print(soup.title)





print(soup.title)
print(soup.find_all('a'))




for link in soup.find_all('a'):
    print(link.get('href'))



print(html)



####Web Crowler - Wikipedia
"""
    1 - Abrir um artigo
    2 - Econtrar o primeiro link no artigo
    3 - Clicar no lik
    4 - Armazenar o line na estrutura article_chain
    5 - Repetir o processo até chegarmos no artigo de filosofia ou ficarmos presos emm um ciclo
"""
"""
    Encontrar o primeiro link no HTML do artigo que está sendo analisado
    Baixar o HTML do artigo que está sendo analisado
    Adicionar o primeiro link deste artigo em article_chain

Existe outro passo que nós não explicitamos anteriormente:

    Pausar por alguns segundos o nosso processo para não exaurir a Wikipedia com requisições.
"""

#VARIAVEIS

page = 'https://pt.wikipedia.org/wiki/Framework'
article_chain = []
search_history = []
target_url = 'https://en.wikipedia.org/wiki/Philosophy'


article_chain.append('TESTE')
article_chain.append('TESTE2')
print(article_chain)
print(len(article_chain))

###
"""

"""
search_history.append('LINK1')
search_history.append('LINK2')
search_history.append('LINK3')
count_links = len(search_history)-1
print(count_links)
print(search_history[count_links])
"""

page = 'https://pt.wikipedia.org/wiki/Framework'
search_history = []
target_url = 'https://en.wikipedia.org/wiki/Philosophy'

search_history.append('LINK1')
search_history.append('LINK2')
search_history.append('LINK3')

def last_position_list(list_source):
    """
    Retorna última posição de uma lista
    """
    last_position = len(list_source)-1
    return last_position

def continue_crawl(search_hist, target, max_steps=25):
    count_links = len(search_history)
    if search_history[int(last_position_list(search_history))] == str(target_url):
        print("Encontramos o artigo final (target):{}!".format(target))
        return False
    elif len(search_history) > max_steps:
        print("A busca se tornou muito longa. Abortando a busca!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("Nós estamos em um artigo que já vimos. Abortando a busca!")
        return False
    else:
        return True
    #UDACITY elif search_history[-1] in search_history[:-1]:
    #ME elif len(search_history) == len(set(search_history)):
    #print(continue_crawl(search_history, target_url))

from bs4 import BeautifulSoup
import requests

def find_first_link(initial_link):
    response = requests.get(initial_link)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.p.a






article_chain = []

while continue_crawl(article_chain, target_url):
     
import time
import urllib

import bs4
import requests


start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"

def find_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")

    # Esta div contém o corpo principal do artigo
    content_div = soup.find(id="mw-content-text")

    # armazena o primeiro link encontrado no artigo, se o artigo não contém
    # nenhum link, este artigo será "none"
    article_link = None

    # Para cada descendente direto de content_div existem parágrafos
    for element in content_div.find_all("p", recursive=False):
        # Encontra a primeira marcação de âncora que seja descendente direto de um parágrafo
        # É importante olhar apenas para os descendentes diretos, pois outros tipos de
        # links, como rodapés e guias de pronunciação, podem ser apresentados antes
        # do primeiro link para um artigo. Esses outros tipos de links, contudo, não
        # são descendentes diretos, pois estão em divs de outras classes.
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break

    if not article_link:
        return

    # Constrói uma URL completa, dada uma URL relativa article_link
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return first_link

def continue_crawl(search_history, target_url, max_steps=25):
    if search_history[-1] == target_url:
        print("Encontramos o artigo final (target)!")
        return False
    elif len(search_history) > max_steps:
        print("a busca se tornou muito longa. Abortando a busca.")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("Estamos em um artigo que já vimos. Abortando a busca.")
        return False
    else:
        return True

article_chain = [start_url]

while continue_crawl(article_chain, target_url):
    print(article_chain[-1])

    first_link = find_first_link(article_chain[-1])
    if not first_link:
        print("Chegamos a um artigo sem links. Abortando a busca.")
        break

    article_chain.append(first_link)

    time.sleep(2)
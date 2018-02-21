from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import time

start_url = "https://pt.wikipedia.org/wiki/Framework"
target_url = "https://en.wikipedia.org/wiki/Philosophy"

def find_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    content_div = soup.find(id="mw-content-text")
    article_link = None

    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break

    if not article_link:
        return

    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return first_link

def last_position_list(list_source):
    """
    Retorna última posição de uma lista
    """
    last_position = len(list_source)-1
    return last_position

def continue_crawl(search_history, target_url, max_steps=25):
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

article_chain = [start_url]

while continue_crawl(article_chain, target_url):
    print(article_chain[-1])

    first_link = find_first_link(article_chain[-1])
    if not first_link:
        print("Artigo sem link. Abortando busca.")
        break

    article_chain.append(first_link)

    time.sleep(2)
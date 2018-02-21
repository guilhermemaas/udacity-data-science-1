#coding:UTF-8
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

print(len(headlines[0])), print(len(headlines[0]) + len(headlines[1])), print(len(headlines[0]) + len(headlines[1]) + len(headlines[2]))

news_ticker = ""
limit_caracteres = 140
count_caracteres = 0
index = 0

for noticias in headlines:
    print("debug: Limite de Caracteres é: {}".format(limit_caracteres))
    print("debug: Notícias adicionados até o momento são: {}".format(news_ticker))
    print("debug: Total de caracteres adicionados até o momento: {}".format(count_caracteres))
    if count_caracteres + len(headlines[index]) >= limit_caracteres:
        print("debug: Limite atingido. Parando adição de caracteres.")
        break
    else:
        #news_ticker.append(linha[index])
        print("debug: Adicionando Noticia: {}".format(headlines[index]))
        news_ticker += headlines[index]
        count_caracteres += (len(headlines[index]))
        index += 1
print(news_ticker)

"""             
index = 0
news_ticker = headlines[index] + " - "
count = len(headlines[index])
print(type(count))
print(count)
print(news_ticker)
print(len(news_ticker))
index = 1
news_ticker += headlines[index] + " - "
print(news_ticker)
"""

print(len("Guilherme"))
string1 = "guilherme"
string2 = "maas"
strint_total = len(string1) + len(string2)
print(strint_total)




# TODO: set news_ticker to a string that contains no more than 140 characters long.
# HINT: modify the headlines list to verify your loop works with different inputs

#def news_ticker(limit):
    total_caracteres = 0
    texto_atual = []
    for string in headlines:
        if total_caracteres + texto_atual[0] >= 140:
            break
        else:
            texto_atual.append(string[0])
            texto_atual += string[0]
#return(texto_atual)    
#print(news_ticker(140))
    
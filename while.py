card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

while sum(hand) <= 17:
    hand.append(card_deck.pop())

print(hand)

#append -> adiciona valores a uma lista
#pop -> Remove valores de uma lista


#Função para pegar números inteiros ao quadrado menores que um int limite
def nearest_square(limit):
    number = 1

    while number ** 2 < limit:
        total = number ** 2
        number += 1
     
    return(total)

test1 = nearest_square(40)
print("Expected result: 36, actual result: {}".format(test1))

print(6*6)
print(39*39)

print(1**2)
print(2**2)
print(3**2)

#Resolução Udacity:
def nearest_square(limit):
    answer = 0
    while (answer+1)**2 < limit:
        answer += 1
    return answer**2

##
#Carregar um navio, até o limite. Exemplo de Break, e gerar uma lista de listas

#Cada item do manifest é um item e seu peso
manifest = [["bananas", 15], ["mattresses", 34], ["dog kennels",42], ["machine that goes ping!", 120], ["tea chests", 10], ["cheeses", 0]]

cargo_weight = 0
cargo_hold = []

for cargo in manifest:
    if cargo_weight >= 100:
        break
    else:
        cargo_hold.append(cargo[0])
        cargo_weight += cargo[1]
print(cargo_hold)
print(cargo_weight)



manifest = [["bananas", 15], ["mattresses", 34], ["dog kennels",42], ["machine that goes ping!", 120], ["tea chests", 10], ["cheeses", 0]]
cargo_weight = 0
cargo_hold = []

for cargo in manifest:
    print("debug: the weight is currently: {}".format(cargo_weight))
    if cargo_weight >= 100:
        print("debug: breaking loop now!")
        break
    else:
        print("debug: adding item: {}".format(cargo[0]))
        print("debug: with weight: {}".format(cargo[1]))
        cargo_hold.append(cargo[0])
        cargo_weight += cargo[1]
    print(cargo_weight)

#A função acima, da Udacity possui um bug que aciona um item a mais. Nesse caso é necessário breakar antes de adicioná-lo. Corrigido:

manifest = [["bananas", 15], ["mattresses", 34], ["dog kennels",42], ["machine that goes ping!", 120], ["tea chests", 10], ["cheeses", 0]]
cargo_weight = 0
cargo_hold = []

for cargo in manifest:
    print("debug: O peso da carga atual é: {}".format(cargo_weight))
    if cargo_weight + cargo[1] >= 100:
        print("debu: Caso seja adicionado o item:" + cargo[0] + "será ultrapassado o limite de carga. Finalizando carregamento.")
        break
    else:
        print("debug: Adicionando item no carregamento: {}".format(cargo[0]))
        print("debug: Peso do item: {}".format(cargo[1]))
        cargo_hold.append(cargo[0])
        cargo_weight += cargo[1]
    print(cargo_weight)

###
#função para adiconar strings a uma variável até atingir limite, a partir  de uma lista
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
        news_ticker += headlines[index] + " "
        count_caracteres += (len(headlines[index]))
        index += 1
print(news_ticker)
print(len(news_ticker))

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
print(len("Guilherme"))
string1 = "guilherme"
string2 = "maas"
strint_total = len(string1) + len(string2)
print(strint_total)
"""


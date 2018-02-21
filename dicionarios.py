#Exemplo de dicionário:

elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}

print(elements['carbon'])

#Adicionar um novo valor:

elements['lithium'] = 3
print(elements['lithium'])
elements['enxofre'] = 3

population = {'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}
print(population)
#print(population['Brasilia'])

###verificar se uma chave existe no dicionário:

if 'Shangai' in population:
    print("Essa cidade existe!")
else:  
    print("Essa cidade não existe!")

population = {'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}
print(population.get('Brasilia', 'Não existe esse país! :('))
>>none
print(population['Brasilia'])
>>    print(population['Brasilia'])
KeyError: 'Brasilia'


Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963, 
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}

for album_title in Beatles_Discography:
    print("title: {}, year: {}".format(album_title, Beatles_Discography[album_title]))

print(Beatles_Discography[album_title])


###Udacity:
def most_prolific(Discography):

    #Vamos criar um dicionário de anos
    #e o número de albuns por ano
    year_dict = {}
    for album, year in Discography.iteritems():
        if year in year_dict:
            year_dict[year]+=1
        else:
            year_dict[year]=1

    #vamos encontrar o ano que tem
    #o maior número de albuns publicados
    #tem formas mais elegantes de fazer isso
    #mas o código abaixo funciona
    max_albums = 0
    max_year = 0
    for year, album_nums in year_dict.iteritems():
        if album_nums > max_albums:
            max_albums = album_nums
            max_year = year
    return max_year




>>> d = {'key1': 'val1', 'key2':'val2'}

>>> # retorna a chave (k) e o valor (v) do dicionário
>>> for k,v in d.items():
...    print(k,v)
...
key2 val2
key1 val1

#Mais de um registro em um dicionário:
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

print(elements.get('unobtainium', 'Theres no such element!'))
print(elements['helium'])

#Procurando informações específicas dentro de dicionários dentreo de dicionários:
print(elements['helium']['weight'])



#Adicionar itens dentro de um dicionario dentro de um dicionario
elements['lithium'] = 3
print(elements['lithium'])

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

elements['enxofre'] = {'number': 3, 'wheight': 2.00895, 'symbol': 'Ex'}
elements['enxofre'] = {'number': 4}
elements['enxofre'] + {'me add 2': 'oi'}

print(elements)



###Quiz - Udacity - Circo voador:
"""Quiz: Registros de um Circo Voador

Um circo voador regular acontece duas ou três vezes por mês. Para cada mês, 
as informações sobre a quantidade de dinheiro recebida em cada evento são salvas em uma lista, 
de modo que os valores aparecem na ordem em que aconteceram. Os dados dos meses são todos coletados em um dicionário chamado monthly_takings.

Para este quiz, escreva uma função total_takings que calcula a soma das receitas de cada circo no ano.
"""
monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}


sum_per_month = {}

for month, values in monthly_takings.items():
    sum_per_month[month] = sum(values)

print(sum_per_month)

#########Função para somar por mês

monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}


def total_takings(month_values):
    pass # TODO: Implemenent this function
    sum_per_month = {}

    for month, values in month_values.items():
        sum_per_month[month] = sum(values)

    return sum_per_month

print(total_takings(monthly_takings))


#######################################
###Função para somar tudo que o circo arrecadou no ano

monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}


def total_takings(month_values):
    pass # TODO: Implemenent this function
    sum_per_month = {}
    total_all_months = 0

    for month, values in month_values.items():
        sum_per_month[month] = sum(values)

    total_all_months = sum(sum_per_month.values())
    
    return total_all_months

print("Total arrecadado pelo circo em um ano. Esperado: 1353. Realizado: {}".format(total_takings(monthly_takings)))








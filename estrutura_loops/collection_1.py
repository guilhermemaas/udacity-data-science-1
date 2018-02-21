#1 - Listas

python_versions = [1.0, 1.5, 1.6, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6]

print(python_versions[0])
print(python_versions[1])
print(python_versions[7])

#Índice negativos -> de traz pra frente

print(python_versions[-1])
print(python_versions[-2])

#Função que retorna valor de uma lista, para quantos dias tem os meses do ano:
def how_many_days(month_number):
    """Returns the number of days in a month.
    WARNING: This function doesn't account for leap years!
    """
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    #todo: return the correct value
    return days_in_month[month_number]
# This test case should print 31, the number of days in the eighth month, August
print(how_many_days(1))

#Slice Lists:

months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

#Cortar o terceiro quadrimestre do ano (o terceiro quarto):

q3 = months[6:9]
print(q3)
print(months)

#Explicação: 6 -> Start Index (Julio, sétimo mês, e sétimo índice) | 9 End Index (Setembro, o nono índice, décimo mês)
#O indexador à esquerda de ":" é onde o corte começa, ou seja, o 6. O corte continua até o segundo Index, o 9.
#Primeira metade:
months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
first_half = months[:6]
print(first_half)
second_half = months[6:]
print(second_half)

####Pegar as últimas 3 datas mais rescentes:

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
eclipse_dates = eclipse_dates[7:]
# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates)

ou 

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
#eclipse_dates = eclipse_dates[7:]
#TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])
>>['November 13, 2012', 'March 20, 2015', 'March 9, 2016']
###

sample_string = "And Now For Something Completely Diferrent"
sample_list = ['Graham', 'John', 'Terry', 'Eric', 'Terry', 'Michael']
print(sample_string[4])
print(sample_list[4])
print(sample_string[12:21])
print(sample_list[2:4])
print(len(sample_string))
print(len(sample_list))
print('thing' in sample_string)
print('Rowan' in sample_list)
#
uma_frase = "Uma Palavra"
print(uma_frase[2])
uma_frase[2] = 'b' #TypeError: 'str' object does not support item assignment
#Strins são imutáveis
#
sample_list = ['Graham', 'John', 'Terry', 'Eric', 'Terry', 'Michael']
print(sample_list[3])
sample_list[3] = 'Guts'
print(sample_list[3])
sample_list[3] = 4
print(sample_list[3])
#enquanto que uma lista pode ser mutável, como acima, onde o índice 3 sofre atualização


dish = ["Spam", "Spam", "Spam", "Spam", "Spam", "Spam", "baked beans", "Spam", "Spam", "Spam", "Spam"]
mr_buns_order = dish
print(dish)
['Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'baked beans', 'Spam', 'Spam', 'Spam', 'Spam']
print(mr_buns_order)
['Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'baked beans', 'Spam', 'Spam', 'Spam', 'Spam']
dish[6] = "Spam" #baked beans are off
print(mr_buns_order)
['Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam']
print(dish)
['Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Spam'],

#Funções embutidas para listas:

len(nome_lista)
#Retorna quantos elementos estão em nome_lista

max(nome_lista) | min(nome_lista)
#Retorna o maior e menor elemento da lista. Podendo mudar a lógica quando temos Strings ou Inteiros

some_list = ['Palavra1', 'Palavraa2', 'Palavraa3', 1, 3, 6]
print(some_list[2])
print(len(some_list))
print(max(some_list)) #>>TypeError: '>' not supported between instances of 'int' and 'str'

python_varieties = ['Burmese Python', 'African Rock Python', 'Ball Python', 'Reticulated Python', 'Angolan Python']
print(max(python_varieties))
print(min(python_varieties))
>>Reticulated Python
>>African Rock Python
#Max e min em listas de string irão retornar por ordem alfabética.

 sorted(some_list)
 #Ordena a Lista

batch_sizes = [15, 6, 89, 34, 65, 35]
print(sorted(batch_sizes))
print(sorted(batch_sizes, reverse=True))
print(batch_sizes)
[6, 15, 34, 35, 65, 89]
[89, 65, 35, 34, 15, 6]
[15, 6, 89, 34, 65, 35]

#Método de junção, Join de listas (Somente Strings):

nautical_directions = "\n".join(['fore', 'aft', 'starboard', "port"])
print(nautical_directions)
fore
aft
starboard
port

names = "-".join(["García", "O'Kelly", "Davis"])
print(names)
García-O'Kelly-Davis

>>> names = ["García" "O'Kelly", "Davis"]
>>> "-".join(names)
"GarcíaO'Kelly-Davis"

##Erro que ocorre quando se tenta fazer join de int e str
>>> stuff = ["thing", 42, "nope"]
>>> " and ".join(stuff)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sequence item 1: expected str instance, int found

##Adicioando valores em uma lista, método append:
nome_completo = ['Guilherme', 'Augusto']
print(nome_completo)
nome_completo.append('Maas')
print(nome_completo)

#Função que retorna os últimos 3 elementos da lista, com basta num imput
def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    # TODO: implement this function
    #total_arguments = [input_list]
    top_three_arguments = input_list[3:]
    
    return top_three_arguments

input_list = [1,2,5,10,25,23]
print (top_three(input_list))


#Função que retorna os 3 maiores elementos da lista, com basta num imput
def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    # TODO: implement this function
    #total_arguments = [input_list]
    top_three_elements = sorted((input_list), reverse = True)[:3]
    
    return top_three_elements

input_list = [2,3,5,6,8,4,2,1]
print (top_three(input_list))

Classe: NumberExtractor
        
class NumberExtractor:

    def top_three(input_list):
        """Retorna uma lista com os três maiores valores de uma lista.

        Se a lista de entrada possuir somente três valores, irá retornar os mesmos de forma decrescente.
        """
        #total_arguments = [input_list]
        top_three_elements = sorted((input_list), reverse = True)[:3]
        
        return top_three_elements

import /NumberExtractor.py
NumberExtractor().top_three([1,2,5,6])


#Função que retorna média dos valores centrais de uma lista com número par de elementos

def median(numbers):
    numbers.sort() 
    if len(numbers) % 2:
        # se a lista tem um número de elementos ímpar,
        # a mediana é o elemento central
        middle_index = int(len(numbers)/2)
        return numbers[middle_index]
    else:
        # se a lista tem um número de elementos par,
        # a mediana é a média dos dois elementos centrais
        right_of_middle = len(numbers)//2 
        left_of_middle = right_of_middle - 1
        return (numbers[right_of_middle] + numbers[left_of_middle])/2



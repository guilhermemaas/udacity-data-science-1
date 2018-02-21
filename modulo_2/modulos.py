import  math

#Função Factorial (Encontra o produto de um inteiro com todos os inteiros menores que ele)
print(math.factorial(4))
>>24

#Por que 4 x 3 x 2 x 1 = 24

import datetime

print(datetime.datetime())

import multiprocessing as mp

print(mp.cpu_count())

###
#Impoprtar somente módulo específico e renomear ele, ou abreviar, ou apelidar:

from csv import reader as csvreader

#Importar um sum módulo:

import os.path


from datetime import datetime


### Função para gerar sena aleatoria com trechos de textos de um arquivo externo.

# Use an import statement at the top

import random

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function here
# It should return a string consisting of three random words 
# concatenated together without spaces

def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)

"""
Outra maneira de fazer isso.
def generate_password():
    return str().join(random.sample(word_list,3))
""" 
    
print(generate_password())

##Exemplo, biblioteca de terceiros
##datetime e timezone

#from datetime #import datetime
import datetime

import pytz

utc = pytz.utc # utc significa "tempo universal coordenado"
ist = pytz.timezone('Asia/Kolkata') # IST é hora padrão da Índia

now = datetime.datetime.now(tz=utc) # é a hora atual em UTC
ist_now = now.astimezone(ist) # é a hora atual em IST.

print(ist_now)
2017-08-25 00:22:22.871886+05:30



print(3+1)

print(1 + 5 + 3 * 3)

#elevar a potência
print(3**2)

#resto da divisão do primeiro número pelo segundo
print(9 % 2)
1
#9/2 = 4, resto = 1

#Arredondar divisão de 2 inteiros
print(15 // 4)
3

print((23+32+64)/3)


#Quiz: Calcular e formatar
#Nesse quiz, você fará alguns cálculos para um colocador de piso. Duas partes de um piso precisam de azulejos. Uma parte mede 9 azulejos de largura por 7 de comprimento, a outra mede 5 azulejos de largura por 7 de comprimento. Os azulejos vêm em pacotes de 6.

#Quantos azulejos são necessários?
#Você compra 17 pacotes de azulejo, contendo 6 azulejos cada. Quantos azulejos irão sobrar?

# Fill this in with an expression that calculates how many tiles are needed.
print((9*7) + (5*7))

# Fill this in with an expression that calculates how many tiles will be left over.
print((17*6) - ((9*7) + (5*7)))

#converter para float
>>> float(3520+3239)
6759.0

#converter para int
>>> int(49.7)
49
>>> int(16/4)
4

>>> print(0.1)
0.1
>>> print(0.1 + 0.1 + 0.1)
0.3


>>> print(5/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero

# O volume atual do reservatório de água (em metros cúbicos)
reservoir_volume = 4.445e8
# A quantidade de precipitação de uma tempestade (em metros cúbicos)
rainfall = 5e6

# diminui a variável precipitação em 10%, devido a escoamento
rainfall *= .9

# adiciona a variável precipitação à variável do volume do reservatório
reservoir_volume += rainfall

# aumenta o reservoir_volume em 5%, por conta das águas pluviais que fluem
# para dentro do reservatório nos dias seguintes à tempestade
reservoir_volume *= 1.05

# diminui o reservoir_volume em 5%, por conta da evaporação 
reservoir_volume *= 0.95

# subtrai 2.5e5 metros cúbicos do reservoir_volume, por conta das águas
# que são canalizadas para regiões áridas.
reservoir_volume -= 2.5e5 

# imprime o novo valor da variável reservoir_volume
print(reservoir_volume)

##
##

#Essas duas atribuições podem ser abreviadas
savings = 514.86
salary = 320.51

#Utilizando atribuição múltipla
savings, salary = 514.86, 320.51

>>> savings, salary = 514.50, 1.500
>>> print (savings, salary)
(514.5, 1.5)

###
###

>>> manila_pop = 1780148
>>> manila_area = 16.56
>>> manila_pop_density = manila_pop/manila_area
>>> print(manila_pop_density)
107496.859903
>>> print(int(manila_pop_density))
107496
>>> manila_pop=1781573
>>> print(int(manila_pop_density))
107496
>>> manila_pop_density = manila_pop/manila_area
>>> print(int(manila_pop_density))
107582
>>>
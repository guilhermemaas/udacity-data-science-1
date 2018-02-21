#Função que calcula o volume de um Cilindro:
#Alutra x quadrado de raio x pi
def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

print(cylinder_volume(10, 3))
>>282.7431

#Função que retorna horas.
#coding:UTF-8
def now():
    import time
    print("Agoras são: " + time.strftime("%H:%M:%S") + ". (@.@)")
    return

now()

#coding:UTF-8
#Função quer print Hello World!
def hello():
    print("Hello World!")
    return

hell()

####
# todo: define a function named `population_density` that takes two arguments, 
# `population` and `land_area` (in square kilometres), and returns a population 
# density calculated from those values.

# Your code goes here!
def population_density(population, land_area):
    return population/land_area

# Here are test cases to verify that your function works as expected:
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}..., actual result: {}".format(expected_result2, test2))

### Função para cálcular densidade demográfica
def population_density(population, land_area):
    population_density = population/land_area
    return population_density

# Here are test cases to verify that your function works as expected:
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}..., actual result: {}".format(expected_result2, test2))


#Função que irá retornar quantas semanas e dias são possíveis informando um inteiro.
def readable_timedelta(days):
    """Funcao pra calcular quantas semanas e dias cabem em um total de dias.
    
        days. int: Total de dias para calculo.
    """
    semanas = days/7
    dias = days - (semanas*7)
    print("{} week(s) and {} days(s).".format(semanas,dias))
    return

readable_timedelta(50)

#Correção:
#coding:UTF-8
def readable_timedelta(days):
    """Exibe o número de semanas e dias em vários dias."""
    #Para pegar o número de semanas, nós usamos a divisão de inteiros
    weeks = days // 7 
    #Para pegar o número de dias que restam, nós usamos %, o ooperador módulo
    remainder = days % 7
    return "{} week(s) and {} days(s).".format(weeks, remainder)

print(readable_timedelta(50))


50 // 7
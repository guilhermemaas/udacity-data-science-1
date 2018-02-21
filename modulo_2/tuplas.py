latlong = (13.4125, 103.83363)
print(type(latlong))
print("A latitude do cliente é: {}".format(latlong[0]))
print("A longitude do cliente é: {}".format(latlong[1]))

##

dimensions = 52, 40, 100
lenght, width, height = dimensions
print(type(dimensions))
print("As dimensões são {}x{}x{}".format(lenght, width, height))

length, width, height = 52, 40, 100

### Tuplas em conjuntos e dict:

world_heritage_locations = {(13.4125, 103.866667): "Angkor Wat",
                            (25.73333, 32.6): "Ancient Thebes",
                            (30.330556, 35.4433330): "Petra",
                            (-13.116667, -72.583333): "Machu Picchu"}

print(world_heritage_locations)


#Exemplo de função que retorna tupla
def first_and_last(sequence):
    """Retorna o primeiro e o último elemento de uma sequência"""
    return sequence[0], sequence[-1]

print(first_and_last(["Spam", "egg", "sausage", "Spam"]))
('Spam', 'Spam')


#Atribuir valores a multiplas variáveis no retorno de uma função.

def first_and_last(sequence):
    """Retorna o primeiro e o último elemento de uma sequência"""
    return sequence[0], sequence[-1]

start, end = first_and_last(["Spam", "egg", "sausage", "Spam"])
print(start)
print(end)


#Função que retorna quantos dias cabem em determinadas horas, também retorna o restante em horas
#print(9 % 2)
#1

def hours2days (period):
    total_days = 0
    resto_horas = 0
    dias = 0, 0
    
    total_days = period // 24
    resto_horas = period % 24
    dias = total_days, resto_horas

    return dias

teste1 = 39
print("O Resultado esperado é (1, 15). O Resultado atual é: {}".format(hours2days(teste1)))

teste2 = 10000
print("O Resultado esperado é (416, 16). O Resultado atual é: {}".format(hours2days(teste2)))


period = 30
total_days = period // 24
resto_horas = period % 24

print(period)
print(total_days)
print(resto_horas)


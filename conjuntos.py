#Funcao que receba uma lista com itens duplicados e retorna a lista removendo-os

paises = ["Brasil", "Brasil", "Paraguai", "Estados Unidos", "Paraguai", "Alemanhã", "Japao", "China", "Japao"]
paises_unicos = sorted(set(paises))
print(paises_unicos)

paises = ["Brasil", "Brasil", "Paraguai", "Estados Unidos", "Paraguai", "Alemanhã", "Japao", "China", "Japao"]

def remove_duplicados(lista):
    return sorted(lista)

print(remove_duplicados(paises))

#Refaturado com logica:

paises = ["Brasil", "Brasil", "Paraguai", "Estados Unidos", "Paraguai", "Alemanhã", "Japao", "China", "Japao"]

def remove_duplicates(source):
    target = []

    for element in source:
        if element not in target:
            target.append(element)
    
    return target

print(sorted(remove_duplicates(paises), reverse = True))

### SET
paises = ["Brasil", "Brasil", "Paraguai", "Estados Unidos", "Paraguai", "Alemanhã", "Japao", "China", "Japao"]
country_set = set(paises)
print(len(paises))
print(len(country_set))

print("Brasil" in paises)
print("Brasil" in country_set)


#Criar um conjunto (set) com todos os números quadrados maiores que 0 menores que 2.000:

def nearest_square(limit):
    squares = set()
    answer = 0 
    while ((answer+1)**2 < limit):
        answer += 1
        squares.add(answer)
    return squares
print(nearest_square(2000))

#squares = nearest_square(2000)
print("Resultado esperado é 1936, e está retornando: {}".format(nearest_square(2000)))
print(nearest_square(2000))

##Solução Udacity
n = 1
while n**2 < 2000:
    squares.add(n**2)
    n += 1





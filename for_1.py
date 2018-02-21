names = ['charlotte hippopotamus turner', 'oliver st. john-mollusc',
         'nigel incubator-jones', 'philip diplodocus mallory']

for name in names:
    print(name.title())

#soma de uma lista:
def list_sum(input_list):
    sum = 0
    # todo: Write a for loop that adds the elements
    # of input_list to the sum variable
    for sum_number in input_list:
        sum += sum_number
        
    return sum



#These test cases check the list_sum works correctly
test1 = list_sum([1, 2, 3])
print("expected result: 6, actual result: {}".format(test1))

test2 = list_sum([-1, 0, 1])
print("expected result: 0, actual result: {}".format(test2))


def tag_count(input_list):
    xml_count = 0
    """
    Funcao recebe como entrada uma lista de strings.
    Conta elementos que possuem tags XML e retorna total.
    """
    for item in input_list:
        if '<' in item and '>' in item:
            xml_count += 1

    return xml_count

input_list = ['<nmmotorista>', 'string', '</nmmotorista>']
count = tag_count(input_list)
print("Resultado Esperado: 2, Resultado: {}".format(count))

#Udacity code:
def tag_count(tokens):
    count = 0
    for token in tokens:
        if token[0] == '<' and token[-1] == '>':
            count += 1
    return count

###Alterando listas com for:
#Adicionar maiúsculas:

names = ['charlotte hippopotamus turner', 'oliver st. john-mollusc',
         'nigel incubator-jones', 'philip diplodocus mallory']

# cria uma nova lista de nomes capitalizados sem modificar a lista original
capitalized_names = [] # cria uma lista nova, vazia
for name in names:
    capitalized_names.append(name.title()) # adiciona elementos à lista

print(names)
print(capitalized_names)
['charlotte hippopotamus turner', 'oliver st. john-mollusc', 'nigel incubator-jones', 'philip diplodocus mallory']
['Charlotte Hippopotamus Turner', 'Oliver St. John-Mollusc', 'Nigel Incubator-Jones', 'Philip Diplodocus Mallory']

# modifica a lista de nomes em ordem (Substituir ao inves de criar uma nova lista)
for index in range(len(names)): # itera sobre os índices da lista de nomes
    names[index] = names[index].title() # modifica cada elemento da lista

#criar uma lista com for
for number in range(4):
    print(number)

print(range(4))

name = "ola"
name = name.title() #Função Title -> Capitalizar string, ou seja, primeira letra da palavra vira maiúscula
print(name)

#Modificando itens da lista acessando seu índice:
names = ['charlotte hippopotamus turner', 'oliver st. john-mollusc', 'nigel incubator-jones', 'philip diplodocus mallory']

for index in range(len(names)):
    names[index] = names[index].title()
    index += 1
print(names)

#Função que retorna HTML
#define the  html_list function
def html_list(strings):
    print("<ul>")
    for li in strings:
        print("<li>" + li + "</li>")
    print("</ul>")

strings = ['first string', 'second string']
html_list(strings)

###A funcao range pode ser utilizada também para repetir ações dentro do for:
for i in range(3):
    print("Camelot!")
Camelot!
Camelot!
Camelot!



def starbox(width, height):
    """imprime uma caixa feita e asteriscos.

    width: comprimento da caixa em caracteres, deve ser ao menos 2
    height: altura da caixa em linhas, deve ser ao menos 2
    """
    print("*" * width) # imprime a ponta superior da caixa

    # imprime os lados da caixa
    for _ in range(height-2):
        print("*" + " " * (width-2) + "*") 

    print("*" * width) # imprime a ponta inferior da caixa




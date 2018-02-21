cast_list = []
file = '/home/swordart/dev/udacity_data_science_1/leitura_arquivo/monty_python_cast.txt'

def create_cast_list(file):
    with open(file) as cast:
        for line in cast:
            #actors.append(line.strip())
            cast_list.append(line.split(None, 1)[0])
    return(cast_list)

create_cast_list(file)
print(cast_list)

#Retornar nome dos atores da série

#Udacity:
def create_cast_list(filename):
    cast_list = []
    # usar with para abrir o arquivo filename
    with open(filename) as f:
    # use a sintaxe do laço for para processar cada linha
    # e adicione o nome do ator a cast_list
        for line in f:
            line_data = line.split(',')
            cast_list.append(line_data[0])
    return cast_list

print(create_cast_list('/home/swordart/dev/udacity_data_science_1/leitura_arquivo/monty_python_cast.txt'))
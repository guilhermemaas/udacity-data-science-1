f = open('/home/swordart/dev/udacity_data_science_1/leitura_arquivo/mdm004.txt','r')
file_data = f.read()
print(file_data)
f.close()
print(type(file_data))

#'r' - Abre arquivo em modo de leitura
#'w' - Abre o arquivo em modo de escrita
#'a' - Abre em  modo de anexação a (append)

files = []
for i in range(10):
    files.append(open('/home/swordart/dev/udacity_data_science_1/leitura_arquivo/mdm004.txt'))
#>>OSError: [Errno 24] Too many open files: '/home/swordart/dev/udacity_data_science_1/leitura_arquivo/mdm004.txt'
print(type(files))

#Com with, depois de executar o bloco de ação em cima do arquivo ele é fechado automaticamene:

with open('/home/swordart/dev/udacity_data_science_1/leitura_arquivo/mdm004.txt','r') as f:
    file_data = f.readline(1)
    print(file_data)


with open('/home/swordart/dev/udacity_data_science_1/leitura_arquivo/mdm004.txt') as mdm004:
    print(mdm004.read(2))
    print(mdm004.read(5))
    print(mdm004.read(10))
"""
"9
45050
"|40,54648
"""

#Ler linhas:
linhas = []

with open('/home/swordart/dev/udacity_data_science_1/leitura_arquivo/mdm004.txt') as mdm004:
    content = mdm004.readlines()

content = [line.rstrip('\n') for line in open('/home/swordart/dev/udacity_data_science_1/leitura_arquivo/mdm004.txt')]

print(content)

linhas = []
with open('/home/swordart/dev/udacity_data_science_1/leitura_arquivo/mdm004.txt') as mdm004:
    for line in mdm004:
        linhas.append(line.strip())

print(linhas[1])
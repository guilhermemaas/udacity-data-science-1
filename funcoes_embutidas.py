#len -> Calcula o tamanho em caracteres, de uma string passada pra ela

udacity_length = len("Udacity")
print(udacity_length)

given_name = "Charlotte"
middle_names = "Hippopotamus"
family_name = "Turner"

name_length = len("Charlotte " + "Hippopotamus " + "Turner") 

driving_licence_character_limit = 28
print(name_length <= driving_licence_character_limit)

##

given_name = "Charlotte"
middle_names = "Hippopotamus"
family_name = "Turner"

name_length = len("Charlotte" + "Hippopotamus" + "Turner") + 2 

driving_licence_character_limit = 28
print(name_length <= driving_licence_character_limit)

#len teste
numero_sorte = len(835)
print(numero_sorte)
Traceback (most recent call last):
  File "/home/swordart/dev/udacity_data_science_1/tempajsdflerhn.py", line 1, in <module>
    numero_sorte = len(835)
TypeError: object of type 'int' has no len()




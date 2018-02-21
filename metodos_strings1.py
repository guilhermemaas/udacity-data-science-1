"charlotte hippopotamus turner".tittle()

full_name = "Charlotte hippopatamus tuerner"
full_name.islower()

>>> full_name = "charlotte hippopatamus tuerner"
>>> full_name.islower()
True
>>> full_name = "Charlotte hippopatamus tuerner"
>>> full_name.islower()
False
>>>

is_integer

number = 4.78
type(number)
str(number).islower()
<type 'float'>
>>> str(number).islower()
False
>>>

#capitalize()
my_name = "GUILHERME"
my_name.capitalize()
'Guilherme'

#casefold()
my_name = @@%%@
my_name.casefold()

#lower()
my_name = "GUILHERME AUGUSTO MAAS"
>>> my_name.lower()
'guilherme augusto maas'

my_name = "GUILHERME AUGUSTO MAAS"
print(my_name.lower())

my_name = "GUILHERME AUGUSTO MAAS"
print(my_name.capitalize())


#center()
#my_name = "Guilherme Augusto Maas"
#center(50[my_name])

#find()
#Sintaxe
#str.find(str, beg=0, end=len(string))
#str -- String que vai ser buscado
#beg -- Índice inicial, 0 por padrão
#end -- Índice final, por padrão o total da string
#Retorno: -1 caso não encontre, e 15, por exemplo, se for a 15 coluna da string.

###

my_name = "Guilherme Augusto Maas"
string_like = "Aug"
print(my_name.find(string_like))
##>>10
#print(my_name.find(string_like, 2)) ???

#count() -> Contar quanta x uma string aparece
"One fish, Two Fish, Red fish, Blue fish.".count('fish')
>>4
route = "route 1, route 2, route 2"
print(route.count('route'))
>>3


prophecy = "And there shall in that time be rumours of things going astray, and there will be a great confusion as to where things really are, and nobody will really know where lieth those little things with the sort of raffia work base, that has an attachment…at this time, a friend shall lose his friends’s hammer and the young shall not know where lieth the things possessed by their fathers that their fathers put there only just the night before around eight o’clock…"
vowel_count = 0
vowel_count = prophecy.count('a') + prophecy.count('A') + prophecy.count('e') + prophecy.count('i') + prophecy.count('o') + prophecy.count('u')
# TODO: set the value of vowel_count to be the number of vowels in prophecy
# Print the final count
print(vowel_count)

#Melhor maneira, primeiro converter tudo para minúsculo:

prophecy = "And there shall in that time be rumours of things going astray, and there will be a great confusion as to where things really are, and nobody will really know where lieth those little things with the sort of raffia work base, that has an attachment…at this time, a friend shall lose his friends’s hammer and the young shall not know where lieth the things possessed by their fathers that their fathers put there only just the night before around eight o’clock…"
lower_prophecy = prophecy.lower()
vowel_count = 0
vowel_count += lower_prophecy.count('a')
vowel_count += lower_prophecy.count('e')
vowel_count += lower_prophecy.count('i')
vowel_count += lower_prophecy.count('o')
vowel_count += lower_prophecy.count('u')
print(vowel_count)

###FORMATAÇÃO DE STRINGS###
#format()
#exemplo, gerar log de um servidor web:
import time
#print(time.strftime("%H:%M:%S"))
user_ip = '192.168.1.25'
url = "http://gmaas/contributions/2"
at = time.strftime("%H:%M:%S")
log_message = "IP address {} accessed {} at {}".format(user_ip, url, at)
print(log_message)
print(log_message.lower())
print(log_message.capitalize())
>>IP address 192.168.1.25 accessed http://gmaas/contributions/2 at 09:57:24
>>ip address 192.168.1.25 accessed http://gmaas/contributions/2 at 09:57:24
>>Ip address 192.168.1.25 accessed http://gmaas/contributions/2 at 09:57:24

city = "Seoul"
high_temperature = 18
low_temperature = 9
temperature_unit = "degrees Celsius"
weather_conditions = "light rain"

#todo rewrite this line to use the format method rather than string concatenation
#alert = "Today's forecast for " + city + ": The temperature will range from " + str(low_temperature) + " to " + str(high_temperature) + " " + temperature_unit + ". Conditions will be " + weather_conditions + "."
alert = "Today's forecast for {}: The temperature will range from {} to {} {}. Conditions will be {}.".format(city, low_temperature, high_temperature, temperature_unit, weather_conditions)


# print the alert
print(alert)


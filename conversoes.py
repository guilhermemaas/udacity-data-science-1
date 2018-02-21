
#    int (inteiro, para números inteiros)
#    float (para números que não são necessariamente números inteiros)
#    bool (boolean, para os valores Verdadeiro ou Falso)
#    str (string, para textos)

#Verificar tipo de objeto
print(type(633))
<type 'int'>

print(type("oi"))
<type 'str'>

print(type(633.0))
<type 'float'>

print("hippo"*12)
hippohippohippohippohippohippohippohippohippohippohippohippo


#Convertendo

count = int(4.0)
print(count)
4
print(type(count))
<type 'int'>


#String a partir de um número:

house_number = 295
street_name = "Pomerode"
town_name = "Timbo City"
print(type(house_number))
address = str(house_number) + " " + street_name + ", " + town_name
print(address)
<type 'int'>
295 Pomerode, Timbo City

#String to Float:
grams_of_sugar = float("35.0")
print grams_of_sugar
print(type(grams_of_sugar))
35.0
<type 'float'>

#Soma de vendas da semana:
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

total_sales = float(mon_sales) + float(tues_sales) + float(wed_sales) + float(thurs_sales) + float(fri_sales)
print(type(total_sales))
print(total_sales)

#printa total
print("This week's total sales: " + str(total_sales) + "." )
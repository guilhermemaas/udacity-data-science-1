#coding:UTF-8

number = 10

if number % 2 == 0:
    print("O número " + str(number) + " é PAR." )
else:
    print("O número " + str(number) + " é IMPAR.")

#

#coding:UTF-8

number = 5

if number % 2 == 0:
    print("O número " + str(number) + " é PAR." )
else:
    print("O número " + str(number) + " é IMPAR.")


###Função estação do ano para com o jardim

def garden_calendar(season):
    if season == "spring":
        print("Time to plant the garden!")
    elif season == "summer":
        print("Time to water de garden!")
    elif season == "autumn" or season == "fall":
        print("Time to stay indoors and drink tea!")
    else:
        print("I don't recognize that season!")

season = "spring"
garden_calendar(season)

#

#phone_balance = 7.62
#bank_balance = 104.39
phone_balance = 12.34
bank_balance = 25
if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10
print(phone_balance)
print(bank_balance)   

#

#altere o numero do experimento!
#number = 145346334
number = 5 #3 sir
if number % 2 == 0:
    print("O numero " + str(number) + " e par.")
else:
    print("O numero " + str(number) + " e impar.")

#
#Terceiro exemplo

#Alterar a idade para experimentar com o preco
age = 105

#Definir os limites de idade para tarifas de onibus
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

#Alterar tarifas de onibus
concession_ticket = 1.25
adult_ticket = 2.50

#Logica do preco do bilhete
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket
message = "Alguem que tem {} anos de idade ira pagar ${} para andar de onibus.".format(age,ticket_price)
print(message)

###Loteria
#pontos = 0

#funcao
def wich_prize(pontos):
    premio = 0
    premiacao = ""

    if pontos <= 50:
        premio = "A wooden rabbit"
    elif pontos >= 51 and pontos <= 150:
        premio = "No prize"
    elif pontos >= 151 and pontos <= 180:
        premio = "A wafer-thin min"
    elif pontos >= 181 and pontos <= 200:
        premio = "A penguin"

    premiacao = "Congratulations! You have won a {}!".format(premio)

    """
    if pontos < 0 and pontos > 200:
        premiacao = "Oh dear, no prize this time."
    """

    return premiacao

print(wich_prize(50))

###Segunda implementação:
def which_prize(points):
    """
    Retorna a mensagem do prêmio adquirido, dado um número de pontos
    """
    if points <= 50:
        return "Congratulations! You have won a wooden rabbit!"
    elif points <= 150:
        return "Oh dear, no prize this time."
    elif points <= 180:
        return "Congratulations! You have won a wafer-thin mint!"
    else:
        return "Congratulations! You have won a penguin!"

#Expressões Booleanas:
if is_raining and is_sunny:
    print("Is there a rainbow?")

#Se (Não está na lista de pedido de remoção de e-maiol) E (Localização seja Estados Unidas OU Canadá) ENTÃO: ENIVEL EMAIL
if (not do_not_email) and (location == "USA" or location == "CAN"):
    send_email()

######Pontua frases

#coding:UTF-8
def punctuate(sentence, phrase_type):
    """
    Cria uma frase pontuada a partir de uma string. Por padrão adiciona um ponto final a frases comuns.abs

    sentence: string, a frase que terá pontuação adicionada.
    phrase_type: string, define que tipo de frase criar.
        "exclamation", "question" e "aside" são valores conhecidos.
    """

    if phrase_type == "exclamation":
        sentence_punct = sentence + "!"
    elif phrase_type == "question":
        sentence_punct = sentence + "?"
    elif phrase_type == "aside":
        sentence_punct = "(" + sentence + ")."
    else:
        sentence_punct = sentence + "."

    return sentence_punct

print(punctuate("OIE PESSOAL", "exclamation"))
print(punctuate("KAPPA PRIDE", "aside"))

#Alternativa:

def punctuate2(sentence, phrase_type):
    if phrase_type == "exclamation":
        return sentence + "!"
    elif phrase_type == "question":
        return sentence + "?"
    elif phrase_type == "aside":
        return "(" + sentence + ")"
    else:
        return sentence + "."

###Calcula a área de superfície dos cilindros que são sólidos ou ocos.

def cylinder_surface_area(radius, height, has_top_and_bottom):
    side_area = height * 6.28 * radius
    if has_top_and_bottom:
        top_area = 3.14 * radius ** 2
        return 2 * top_area + side_area
    else:
        return side_area

### Loteria/Bingo 2
#Aqui está a nossa solução - primeiro definimos prize = None, depois, atualizamos prize se os pontos o exigirem. 
#Finalmente, usamos o valor real de prize para imprimir uma mensagem quando houver um prêmio, e uma mensagem quando não houver prêmio.

def which_prize2(points):
    """
    Retorna a mensagem do prêmio adquirido, dado um número de pontos
    """
    prize = None
    if points <= 50:
        prize = "a wooden rabbit"
    elif 150 <= points <= 180:
        prize = "a wafer-thin mint"
    elif points >= 181:
        prize = "a penguin"
    if prize:
        return "Congratulations! You have won " + prize + "!"
    else:
        return "Oh dear, no prize this time."

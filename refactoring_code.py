
my_answers = [2, "gato", 5, "bola", 6]
answers = [2, "gato", 4, "quadrado", 6]

def check_answers(my_answers,answers):
    """
    Checa as cinco respostas fornecidas por um quiz de múltipla escolha e retorna os resultados.
    """
    results= [None, None, None, None, None]
    if my_answers[0] == answers[0]:
        results[0] = True
    elif my_answers[0] != answers[0]:
        results[0] = False
    if my_answers[1] == answers[1]:
        results[1] = True
    elif my_answers[1] != answers[0]:
        results[1] = False
    if my_answers[2] == answers[2]:
        results[2] = True
    elif my_answers[2] != answers[2]:
        results[2] = False
    if my_answers[3] == answers[3]:
        results[3] = True
    elif my_answers[3] != answers[3]:
        results[3] = False
    if my_answers[4] == answers[4]:
        results[4] = True
    elif my_answers[4] != answers[4]:
        results[4] = False
    print(results)
    count_correct = 0
    count_incorrect = 0
    for result in results:
        if result == True:
            count_correct += 1
        if result != True:
            count_incorrect += 1
    if count_correct/5 > 0.7:
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    elif count_incorrect/5 >= 0.3:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."

print(check_answers(my_answers, answers))


my_answers = [2, "gato", 5, "bola", 6]
answers = [2, "gato", 4, "quadrado", 6]

def correcao(my_answer, correct_answer):
    if my_answer == correct_answer:
        result = True
    else:
        result = False
    return(result)

#Refatorada
def check_answers(my_answers,answers):
    """
    Checa as cinco respostas fornecidas por um quiz de múltipla escolha e retorna os resultados.
    """
    answer_index = 0
    results= [None, None, None, None, None]
    count_correct = 0
    count_incorrect = 0

    for question in my_answers:

        if my_answers[answer_index] == answers[answer_index]:
            results[answer_index] = True
            count_correct += 1
        else:
            results[answer_index] = False
            count_incorrect += 1
        answer_index += 1

    if count_correct/5 >= 0.7:
        return "Parabéns, você passou! Seu score é: " + str(count_correct) + " de of 5."
    elif count_incorrect/5 >= 0.3:
        return "Infelizmente você não passou! Seu score é: " + str(count_correct) + " de of 5"

print(check_answers(my_answers, answers))
        
###Refatorada 2.0

my_answers = [1, 2, 3, 4, 5]
answers = ["badger","badger","badger","badger","badger"]

def correcao(my_answer, correct_answer):
    """
    Recebe resposta esperada e realizada.
    Realiza comparacao e retorna resultado True ou False.
    """
    if my_answer == correct_answer:
        result = True
    else:
        result = False
    return(result)

def check_answers(my_answers,answers):
    """
    Checa as cinco respostas fornecidas por um quiz de múltipla escolha e retorna os resultados.
    Recebe as respostas realizadas e esperadas. Processa e Devolve se passou sim ou nao jutamente de resultado.
    my_answers -> Lista de respostas enviadas
    answers -> Lista de respostas esperadas.
    """
    answer_index = 0
    count_correct = 0
    count_incorrect = 0
    my_answer = ""
    correct_answer = ""

    for question in my_answers:

        if correcao(my_answers[answer_index],answers[answer_index]) == True:
            count_correct += 1
        else:
            count_incorrect += 1

        answer_index += 1

    if count_correct/5 >= 0.7:
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    elif count_incorrect/5 >= 0.3:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."

print(check_answers(my_answers, answers))


###Refatoramento Udacity:
my_answers = [1, 2, 3, 4, 5]
answers = ["badger","badger","badger","badger","badger"]

def check_answer(my_answer, answer):
    if my_answer == answer:
        return True
    else:
        return False

def check_answers(my_answers,answers):
    #Checks the five answers provided to a multiple choice quiz and returns the results.
    results = []
    for i in range(len(my_answers)):
        results.append(check_answer(my_answers[i], answers[i]))
    count_correct = 0

    for result in results:
        if result:
            count_correct += 1

    if count_correct/len(results) > 0.7:
        return "Congratulations, you passed the test!"
    elif (len(results) - count_correct)/len(results) >= 0.3:
        return "Unfortunately, you did not pass."

print(check_answers(my_answers, answers))


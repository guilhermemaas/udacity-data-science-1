#coding:UTF-8
### Notas de avalição de produtos por clientes:
"""
Aqui estão nossas quatro etapas:

    -Pegue cada uma das pontuações brutas e converta cada uma delas para um tipo numérico. Entrada: pontuação como string/float/int. 
    Saída: pontuação como float or int.
    -Escolha os 3 valores médios do conjunto de 5 pontuações. Entrada: 5 pontuações como float or int. Saída: 3 pontuações (mesmo tipo).
    -Pegue a média das três pontuações. Entrada: 3 pontuações como float or int. Saída: 1 pontuação média (float).
    -Escolha a palavra correta para a classificação da pontuação média. Entrada: pontuação média como float. Saída: Avaliação como uma string.
"""
def convert_to_numeric(score):
    """
    Converte a pontuação para um tipo numérico.abs
    """
    converted_score = float(score) 
    
    return converted_score

def sum_of_middle_three(score1,score2,score3,score4,score5):
    """
    Encontra a soma dos três valores médios dos cinco dados
    """
    min_score = min(score1,score2,score3,score4,score5)
    max_score = max(score1,score2,score3,score4,score5)
    sum = score1 + score2 + score3 + score4 + score5 - max_score - min_score
    return sum

def score_to_rating_string(av_score):
    """
    Converte a pontuação média, que deve estar entre 0 e 5,
     em uma classificação.
    """
    if av_score < 1:
        rating = "Horrivel"
    elif av_score < 2:
        rating = "Ruim"
    elif av_score < 3:
        rating = "OK"
    elif av_score < 4:
        rating = "Bom"
    else:          #Usando mais no final, todos os casos possíveis são pegos
        rating = "Excelente"
    return rating

def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Transforma cinco notas(score) em uma avaliação a partir dos três valores médios
    das cinco notas, atribuindo a essa média uma avalição escrita.
    """

    #ETAPA 1: converter as notas em números:
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #ETAPA 2 e 3: encontrar a média das três notas médias
    average_score = sum_of_midle_three(score1,score2,score3,score4,score5)/3 #(soma das três notas médias)/3

    #ETAPA 4: transformar a nota média em uma avaliação
    rating = score_to_rating_string(average_score)

    return rating

print(scores_to_rating("1","2.5","4","2","5"))


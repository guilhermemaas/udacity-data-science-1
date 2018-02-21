def box(width, height, symbol="#"):
    """Imprimir uma caixa composta de asteriscos ou algum outro caractere.

    width: Largura da caixa em caracteres, deve ser pelo menos 2
    height: Altura da caixa em linhas, deve ser pelo menos 2
    symbol: Uma única sequência de caracteres usada para desenhar as bordas da caixa
    """
    print(symbol * width) # imprimir a borda superior da caixa

    # print sides of box
    for _ in range(height-2):
        print(symbol + " " * (width-2) + symbol)

    print(symbol * width) # imprimir a borda inferior da caixa

#Para definir um valor padrão adicionar na declaração da função a variável fixa como acima: symbol="#"
print(box(10, 10))


##
def print_list(l, numbered=False, bullet_character="-"):
    """Prints a list on multiple lines, with numbers or bullets
    
    Arguments:
    l: The list to print
    numbered: set to True to print a numbered list
    bullet_character: The symbol placed before each list element. This is
                      ignored if numbered is True.
    """
    for index, element in enumerate(l):
        if numbered:
            print("{}: {}".format(index+1, element))
        else:
            print("{} {}".format(bullet_character, element))
            

print(print_list(["cats", "in", "space"], False, "*"))
print(print_list(["cats", "in", "space"], True))
print(print_list(["cats", "in", "space"]))


###
def todo_list(new_task, base_list=['wake up']):
    base_list.append(new_task)
    return base_list

print(todo_list("check the mail"))

print(todo_list("begin orbital transfer"))
salario = 2000


def salario_bonus(bonus, lista):
    global salario # global é utilizado para 
    # lista.append(2) # por ser um objeto mutavel, tudo feito de alteração na lista é refletido no objeto do lado de fora
    lista_aux = lista.copy() # necessário criar uma cópia para não afetar um objeto mutável
    lista_aux.append(2) 
    print(f'lista aux = {lista_aux}')
    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus(500, lista)
print(salario_com_bonus) #2500
print(lista)
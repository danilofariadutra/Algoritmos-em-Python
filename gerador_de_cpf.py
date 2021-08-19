from random import randint as rd

def gera_digito():
    cpf = []
    cpf_multi = []
    counter = soma = digito = 0
    qtd_digitos = 10
    
    # Gera os 9 primeiros dígitos aleatórios
    for pos in range(0, 9, 1):
        cpf.append(rd(0, 9))
    
    # Gera os dois digitos verificadores (10º dígito e o 11º dígito)
    for digitos_verificadores in range(0, 2):
        for pos in range(qtd_digitos, 1, -1):    
            cpf_multi.append(cpf[counter] * pos)
            soma += cpf_multi[counter]   
            counter += 1
        # Verifica o RESTO da operação: Resto da SOMA da multiplicação dividido por 11; Caso seja < 2, dígito = 0, senão dígito é 11 - RESTO
        if soma % 11 < 2:
            digito = 0
        else:
            digito = 11 - soma % 11    
        cpf.append(digito)
        soma = counter = digito = 0
        qtd_digitos += 1
        cpf_multi = []
    
    # Formata a string
    for position, numero in enumerate(cpf):
        if position % 3 == 0 and position != 9 and position != 0:
            print('.', end='')
        elif position == 9:
            print('-', end='')
        print(numero, end='')
    
gera_digito()

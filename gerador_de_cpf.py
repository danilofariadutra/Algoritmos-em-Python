'''
Informações sobre o CPF:

O antepenúltimo dígito (o que está representado pelo “X” em 000.000.00X-00) indica o estado de origem.

0. Rio Grande do Sul
1. Distrito Federal, Goiás, Mato Grosso, Mato Grosso do Sul e Tocantins
2. Amazonas, Pará, Roraima, Amapá, Acre e Rondônia
3. Ceará, Maranhão e Piauí
4. Paraíba, Pernambuco, Alagoas e Rio Grande do Norte
5. Bahia e Sergipe
6. Minas Gerais
7. Rio de Janeiro e Espírito Santo
8. São Paulo
9. Paraná e Santa Catarina

Validador de CPF: https://www.4devs.com.br/validador_cpf
'''

from random import randint as rd

def gera_digito():
    
    estado = int(input('Qual a origem do Estado do CPF Gerado?\n[0] Rio Grande do Sul\n[1] Distrito Federal, Goiás, Mato Grosso, Mato Grosso do Sul e Tocantins\n[2] Amazonas, Pará, Roraima, Amapá, Acre e Rondônia\n[3] Ceará, Maranhão e Piauí\n[4] Paraíba, Pernambuco, Alagoas e Rio Grande do Norte\n[5] Bahia e Sergipe\n[6] Minas Gerais\n[7] Rio de Janeiro e Espírito Santo\n[8] São Paulo\n[9] Paraná e Santa Catarina\n[Qualquer outro valor para sair]: '))
    
    cpf = []
    cpf_multi = []
    counter = soma = digito = 0
    qtd_digitos = 10
    
    # Gera os 9 primeiros dígitos aleatórios
    if estado <= 9:
        for pos in range(0, 9, 1):
            if pos == 8:
                cpf.append(estado)
            else:
                cpf.append(rd(0, 9))        
    else:        
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

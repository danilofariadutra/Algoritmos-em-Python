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
import PySimpleGUI as sg

cpf = []
cpf_multi = []
counter = soma = digito = 0
qtd_digitos = 10
cpf_final = ''
        
sg.theme('SystemDefault')  
layout = [  [sg.Text('Origem do CPF por Estado\n\n0. Rio Grande do Sul\n1. Distrito Federal, Goiás, Mato Grosso, Mato Grosso do Sul e Tocantins\n2. Amazonas, Pará, Roraima, Amapá, Acre e Rondônia\n3. Ceará, Maranhão e Piauí\n4. Paraíba, Pernambuco, Alagoas e Rio Grande do Norte\n5. Bahia e Sergipe\n6. Minas Gerais\n7. Rio de Janeiro e Espírito Santo\n8. São Paulo\n9. Paraná e Santa Catarina')],
            [sg.Text('Digite o número do Estado: ', pad=(3, 20)), sg.Input(size=(4,0), key='estado')],
            [sg.Text('CPF'), sg.Input('', key='campo_cpf', size=(15,0)), sg.Text('', size=(60,0), key='validacao')],
            [sg.Text('                               '),sg.Button('GERAR CPF'), sg.Button('VALIDAR CPF'), sg.Button('LIMPAR'), sg.Button('SAIR', key='sair')],
            [sg.Text('Desenvolvido por Danilo Dutra', pad=(130,0))],
        ]

window = sg.Window('Gerador e Validador de CPF', layout, size=(480, 350))
window.SetIcon('C:/Users/danilo.dutra/Desktop/Python/gerador_de_cpf_gui/ico/ico_2.ico')

while True:    
    event, values = window.read()   

    if event == sg.WIN_CLOSED or event=='Exit' or event == 'sair':
        break    

    if event == 'LIMPAR':        
        soma = counter = 0        
        qtd_digitos = 10
        cpf_multi = []
        counter = soma = digito = 0
        cpf_final = ''
        qtd_digitos = 10
        window['estado']('')
        window['campo_cpf']('')
        window['validacao']('')
    
    if event == 'VALIDAR CPF':        

        # FIXME: Formata o número quando é gerado automaticamente
        if '.' in values['campo_cpf'] or '-' in values['campo_cpf']:
            cpf = str(values['campo_cpf'])
            for caractere in cpf:                
                if caractere == '.' or caractere == '-':
                    continue
                else:
                    cpf += caractere
            cpf = cpf[14:]            
            print(cpf)
        else:
            cpf = values['campo_cpf']
        # FIXME: ATÉ AQUI

                
        if cpf == '':
            window['validacao']('Campo vázio. Digite um CPF')
        else:            
            digito = 9
            digitos_verificadores = ''
            try:
                for digitos_verificadores in range(0, 2):
                    for pos in range(qtd_digitos, 1, -1):  
                        cpf_multi.append(int(cpf[counter]) * pos)                    
                        #print(pos, ' x ', cpf[counter], ' = ', cpf_multi[counter], ' | ', end='')
                        soma += int(cpf_multi[counter])
                        counter += 1 
                    digito_verificador = soma % 11
                    
                    # Se o digito verificador for menor que 2, ele é igual a 0
                    if digito_verificador < 2:
                        digito_verificador = 0
                    else:
                        digito_verificador = 11 - soma % 11
                    
                    if digito_verificador == int(cpf[digito]):                        
                        window['validacao']('CPF Válido')
                        digito += 1
                        qtd_digitos += 1
                        soma = counter = digito_verificador = 0
                        cpf_multi.clear()
                    else:                        
                        window['validacao']('CPF Inválido')                                         
                        break                    
            except:
                if len(cpf) != 11:
                    window['validacao']('Formato de CPF inválido')
                else:
                    window['validacao']('Função inválida')
            soma = counter = 0
            qtd_digitos = 10
                    
        cpf_multi.clear()
        counter = soma = digito = 0
        cpf = ''
        qtd_digitos = 10        
        window['estado']('')
    
    if event == 'GERAR CPF':
        window['validacao']('')
        cpf = []
        cpf_multi = []
        counter = soma = digito = 0
        cpf_final = ''
        qtd_digitos = 10        
        
        # Gera os 9 primeiros dígitos aleatórios
        if values['estado'] == '':
            estado = rd(0, 9)
            window['estado'](estado)
        else:
            estado = int(values['estado'])
        
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
                cpf_final+= '.'
            elif position == 9:
                cpf_final+= '-'                            
            cpf_final += str(numero) # concatena os números            
    
    window['campo_cpf'](cpf_final) # Atualiza e printa o cpf no Input (campo_cpf)
    cpf = cpf_final
    cpf_final = '' # Limpa o CPF antigo
    
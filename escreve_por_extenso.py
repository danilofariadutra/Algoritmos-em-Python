'''
# Desenvolvido por Danilo Faria Dutra
# Script que escreve por extenso um valor digitado...
Ex.: Você digita "529" (Sem aspas) e o script retorna: "quinhentos e vinte e nove"
'''
numero = '';

while len(numero) < 4:
    numero = input('Digite um número (Digite um valor acima de 999 ou 0 para sair): ')

    if numero == 's' or len(numero) > 3:
        print('Até mais...')
        break

    def unidade(unidade):
        if unidade == '1':
            unidade = 'um'  
        elif unidade == '2':
            unidade = 'dois'
        elif unidade == '3':
            unidade = 'três'
        elif unidade == '4':
            unidade = 'quatro'
        elif unidade == '5':
            unidade = 'cinco'
        elif unidade == '6':
            unidade = 'seis'
        elif unidade == '7':
            unidade = 'sete'
        elif unidade == '8':
            unidade = 'oito'
        elif unidade == '9':
            unidade = 'nove'

        return unidade

    def dezenaDez(dezenaDez):           
        if dezenaDez == '1':
            dezenaDez = 'onze'
        elif dezenaDez == '2':
            dezenaDez = 'doze'
        elif dezenaDez == '3':
            dezenaDez = 'treze'
        elif dezenaDez == '4':
            dezenaDez = 'quatorze'
        elif dezenaDez == '5':
            dezenaDez = 'quinze'
        elif dezenaDez == '6':
            dezenaDez = 'dezesseis'
        elif dezenaDez == '7':
            dezenaDez = 'dezessete'
        elif dezenaDez == '8':
            dezenaDez = 'dezoito'
        elif dezenaDez == '9':
            dezenaDez = 'dezenove'
        
        return dezenaDez

    def dezena(dezena):
        if dezena == '0':
            dezena = 'dez'      
        elif dezena == '2':
            dezena = 'vinte'        
        elif dezena == '3':
            dezena = 'trinta'
        elif dezena == '4':
            dezena = 'quarenta'
        elif dezena == '5':
            dezena = 'cinquenta'
        elif dezena == '6':
            dezena = 'sessenta'
        elif dezena == '7':
            dezena = 'setenta'
        elif dezena == '8':
            dezena = 'oitenta'
        elif dezena == '9':
            dezena = 'noventa'

        return dezena

    def centena(centena):   
        if centena == '0':
            centena = 'cem' 
        elif centena == '1':
            centena = 'cento'
        elif centena == '2':
            centena = 'duzentos'
        elif centena == '3':
            centena = 'trezentos'
        elif centena == '4':
            centena = 'quatrocentos'
        elif centena == '5':
            centena = 'quinhentos'
        elif centena == '6':
            centena = 'seicentos'
        elif centena == '7':
            centena = 'setecentos'
        elif centena == '8':
            centena = 'oitocentos'
        elif centena == '9':
            centena = 'novecentos'

        return centena

    # imprime valor de 1 a 9
    if len(numero) == 1:
        print(str(unidade(numero[0])))

    # imprime valor de 11 a 19
    if len(numero) == 2 and numero[0] == '1' and numero[1] != '0':
        print(str(dezenaDez(numero[1])))    
    elif len(numero) == 2 and numero[0] != '1' and numero[1] != '0':
        print(str(dezena(numero[0])) + ' e ' + str(unidade(numero[1])))

    # imprime valor decimal com final 0     
    if len(numero) == 2 and numero[0] != '1' and numero[1] == '0':
        print(str(dezena(numero[0])))

    # imprime valores centenários
    # imprime valores centenários com unidades de 1 a 9. Ex.: 109, 204, 305, 402...
    if len(numero) == 3 and numero[0] == '1' and numero[1] == '0' and numero[2] == '0':
        print(str(centena(numero[2])))
    elif len(numero) == 3 and numero[0] != '1' and numero[1] == '0' and numero[2] == '0':
        print(str(centena(numero[0])))
    elif len(numero) == 3 and numero[1] == '0' and numero[2] != '0':
        print(str(centena(numero[0])) + ' e ' + str(unidade(numero[2])))

    # imprime valores centenários com decimais de 11 a 19. Ex.: 119, 212, 315...
    if len(numero) == 3 and numero[1] == '1' and numero[2] == '0':
        print(str(centena(numero[0]) + ' e ' + str(dezena(numero[2]))))
    elif len(numero) == 3 and numero[1] == '1' and numero[2] != '0':
        print(str(centena(numero[0]) + ' e ' + str(dezenaDez(numero[2]))))

    # imprime números valores de 120 ou mais, com final 0
    if len(numero) == 3 and numero[1] != '0' and numero[1] != '1' and numero[2] == '0':
        print(str(centena(numero[0]) + ' e ' + str(dezena(numero[1]))))
    #imprime números centenários com decimais e unidades
    if len(numero) == 3 and numero[1] != '0' and numero[1] != '1' and numero[2] != '0':
        print(str(centena(numero[0])) + ' e ' + str(dezena(numero[1])) + ' e ' + str(unidade(numero[2])))
    

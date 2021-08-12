'''
# Desenvolvido por Danilo Faria Dutra
# Script que escreve por extenso um valor digitado...
Ex.: Você digita "529" (Sem aspas) e o script retorna: "quinhentos e vinte e nove"
'''

from numeros import numeros as nm

numero = ''

while len(numero) < 4:
    numero = input('Digite um número (Digite um valor acima de 999 ou 0 para sair): ').lower()

    if numero == 's' or len(numero) > 3:
        print('Até mais...')
        break
    
    # imprime valor de 1 a 9
    if len(numero) == 1:
        print(str(nm.unidade(numero[0])))

    # imprime valor de 11 a 19
    if len(numero) == 2 and numero[0] == '1' and numero[1] != '0':
        print(str(nm.dezenaDez(numero[1])))    
    elif len(numero) == 2 and numero[0] != '1' and numero[1] != '0':
        print(str(nm.dezena(numero[0])) + ' e ' + str(nm.unidade(numero[1])))

    # imprime valor decimal com final 0     
    if len(numero) == 2 and numero[0] != '1' and numero[1] == '0':
        print(str(nm.dezena(numero[0])))

    # imprime valores centenários
    # imprime valores centenários com unidades de 1 a 9. Ex.: 109, 204, 305, 402...
    if len(numero) == 3 and numero[0] == '1' and numero[1] == '0' and numero[2] == '0':
        print(str(nm.centena(numero[2])))
    elif len(numero) == 3 and numero[0] != '1' and numero[1] == '0' and numero[2] == '0':
        print(str(nm.centena(numero[0])))
    elif len(numero) == 3 and numero[1] == '0' and numero[2] != '0':
        print(str(nm.centena(numero[0])) + ' e ' + str(nm.unidade(numero[2])))

    # imprime valores centenários com decimais de 11 a 19. Ex.: 119, 212, 315...
    if len(numero) == 3 and numero[1] == '1' and numero[2] == '0':
        print(str(nm.centena(numero[0]) + ' e ' + str(nm.dezena(numero[2]))))
    elif len(numero) == 3 and numero[1] == '1' and numero[2] != '0':
        print(str(nm.centena(numero[0]) + ' e ' + str(nm.dezenaDez(numero[2]))))

    # imprime números valores de 120 ou mais, com final 0
    if len(numero) == 3 and numero[1] != '0' and numero[1] != '1' and numero[2] == '0':
        print(str(nm.centena(numero[0]) + ' e ' + str(nm.dezena(numero[1]))))
    # imprime números centenários com decimais e unidades
    if len(numero) == 3 and numero[1] != '0' and numero[1] != '1' and numero[2] != '0':
        print(str(nm.centena(numero[0])) + ' e ' + str(nm.dezena(numero[1])) + ' e ' + str(nm.unidade(numero[2])))
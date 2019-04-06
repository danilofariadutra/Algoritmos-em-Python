#Código by Danilo Dutra

x = []
y = []
z = []
n = []
valores = []
question = 'n/a'
a1, a2, b1, b2, c1, c2, n1, n2, calcD, calcDx, calcDy, calcDz, dx, dy, dz, op1, op2, q, q2 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0


for c in range(3):
    x.append(int(input(f'Digite os números "X{c+1}": ')))
for c in range(3):
    y.append(int(input(f'Digite os números "Y{c+1}": ')))
for c in range(3):
    z.append(int(input(f'Digite os números "Z{c+1}": ')))
for c in range(3):
    n.append(int(input(f'Digite os números "N{c+1}": ')))

print('Sua Matriz é:\n')
for c in range(3):
    print('[', x[c], ' | ', y[c], ' | ', z[c], ' | ', n[c], ' ]' )

#Multiplica os valores da matriz D
a1 = x[0] * y[1] * z[2]
b1 = y[0] * z[1] * x[2]
c1 = z[0] * x[1] * y[2]
#FIM da Multiplicação

# Conversão de sinais se for necessário
a2 = z[0] * y[1] * x[2]
#inverte os sinais de A
if a2 > 0:
    a2 *= -1
else:
    a2 *= -1

b2 = x[0] * z[1] * y[2]
#inverte os sinais de B
if b2 > 0:
    b2 *= -1
else:
    b2 *= -1

c2 = y[0] * x[1] * z[2]

#inverte os sinais de C
if c2 > 0:
    c2 *= -1
else:
    c2 *= -1
# FIM Conversão de sinais

#calculo da variavel D
calcD = a1 + b1 + c1 + a2 + b2 + c2
print('Este é Calculo D: ', calcD)
#FIM CalcD

#--------------------------------------
#Multiplica os valores da matriz Dx
a1 = n[0] * y[1] * z[2]
b1 = y[0] * z[1] * n[2]
c1 = z[0] * n[1] * y[2]
#FIM da Multiplicação

# Conversão de sinais se for necessário
a2 = z[0] * y[1] * n[2]
#inverte os sinais de A
if a2 > 0:
    a2 *= -1
else:
    a2 *= -1

b2 = n[0] * z[1] * y[2]
#inverte os sinais de B
if b2 > 0:
    b2 *= -1
else:
    b2 *= -1

c2 = y[0] * n[1] * z[2]

#inverte os sinais de C
if c2 > 0:
    c2 *= -1
else:
    c2 *= -1
# FIM Conversão de sinais

#calculo da variavel Dx
calcDx = a1 + b1 + c1 + a2 + b2 + c2
print('Este é Calculo dX:', calcDx)
#FIM CalcDx
#--------------------------------------
#Multiplica os valores da matriz Dy
a1 = x[0] * n[1] * z[2]
b1 = n[0] * z[1] * x[2]
c1 = z[0] * x[1] * n[2]
#FIM da Multiplicação

# Conversão de sinais se for necessário
a2 = z[0] * n[1] * x[2]
#inverte os sinais de A
if a2 > 0:
    a2 *= -1
else:
    a2 *= -1

b2 = x[0] * z[1] * n[2]
#inverte os sinais de B
if b2 > 0:
    b2 *= -1
else:
    b2 *= -1

c2 = n[0] * x[1] * z[2]

#inverte os sinais de C
if c2 > 0:
    c2 *= -1
else:
    c2 *= -1
# FIM Conversão de sinais

#calculo da variavel Dy
calcDy = a1 + b1 + c1 + a2 + b2 + c2
print('Este é Calculo dY: ', calcDy)
#FIM CalcDy

#----------------------------------
#Multiplica os valores da matriz Dz
a1 = x[0] * y[1] * n[2]
b1 = y[0] * n[1] * x[2]
c1 = n[0] * x[1] * y[2]
#FIM da Multiplicação

# Conversão de sinais se for necessário
a2 = n[0] * y[1] * x[2]
#inverte os sinais de A
if a2 > 0:
    a2 *= -1
else:
    a2 *= -1

b2 = x[0] * n[1] * y[2]
#inverte os sinais de B
if b2 > 0:
    b2 *= -1
else:
    b2 *= -1

c2 = y[0] * x[1] * n[2]

#inverte os sinais de C
if c2 > 0:
    c2 *= -1
else:
    c2 *= -1
# FIM Conversão de sinais

#calculo da variavel D
calcDz = a1 + b1 + c1 + a2 + b2 + c2
print('Este é Calculo dZ: ', calcDz)
#FIM CalcD

#----------------------------------
# Divisões

# Divisão DX

dx = calcDx / calcD
dy = calcDy / calcD
dz = calcDz / calcD

print(f'Esta é a solução X:{dx}, Y:{dy}, Z{dz}')

question = str(input('Existe uma equação: ')).upper().strip()
if 'S' in question:
    q = int(input('Quantos valores vão ser inseridos? '))

    for c in range(q):
        valores.append(int(input(f'Digite o valor {c}: ')))

    if q % 2 == 1:
        q2 = int(input('Quantos valores serão adicionados a primeira parte da equação? '))
        if q2 != 2:
            op1 = valores[0]
            op = str(input('Qual a segunda operação? [ +  - , * , / ]'))
            if op is '+':
                op2 = valores[1] + valores[2]
            elif op is '*':
                op2 = valores[1] * valores[2]
            elif op is '/':
                op2 = valores[1] / valores[2]
            else:
                op2 = valores[1] - valores[2]
        else:
            op2 = valores[2]
            op = str(input('Qual a primeira operação? [ +  - , * , / ]'))
            if op is '+':
                op1 = valores[0] + valores[1]
            elif op is '*':
                op1 = valores[0] * valores[1]
            elif op is '/':
                op1 = valores[0] / valores[1]
            else:
                op1 = valores[0] - valores[1]
    else:
        op = str(input('Qual a primeira operação? [ +  - , * , / ]'))
        if op is '+':
            op1 = valores[0] + valores[1]
        elif op is '*':
            op1 = valores[0] * valores[1]
        elif op is '/':
            op1 = valores[0] / valores[1]
        else:
            op1 = valores[0] - valores[1]

        op = str(input('Qual a segunda operação? [ +  - , * , / ]'))
        if op is '+':
            op2 = valores[1] + valores[2]
        elif op is '*':
            op2 = valores[1] * valores[2]
        elif op is '/':
            op2 = valores[1] / valores[2]
        else:
            op2 = valores[1] - valores[2]

    q = op1 / op2

    print(f'Estes são os valores X:{dx}, Y:{dy}, Z{dz}')
    print(f'O Resultado da Equação é: {q}')

#Caso queira mostrar os valores:
#print('Este é A1: ', a1)
#print('Este é B1: ', b1)
#print('Este é C1: ', c1)
#print('Este é A2: ', a2)
#print('Este é B2: ', b2)
#print('Este é C2: ', c2)

print('Este é o Resultado de D: ', calcD)
print('Este é o Resultado de dX: ', calcDx)
print('Este é o Resultado de dY: ', calcDy)
print('Este é o Resultado de dZ: ', calcDz)
print('Este é X: ', dx)
print('Este é Y: ', dy)
print('Este é Z: ', dz)
print(f'Estes são os valores X:{dx}, Y:{dy}, Z{dz}')

#Código by Danilo Dutra
# Capítulo 5: Repetições

# Exercício 5.1

x = 1
while x <100:
    print(x)
    x += 1

# Exercício 5.2

y = 50
while y <= 100:
    print(y)
    y += 1


# Exercício 5.3

print('Contagem regressiva para lançamento do foguete')
w = 10
while w >= 0:
    print(w)
print('Decolar!')

#

# Exercício 5.4 

fim = int(input('Digite o último número a imprimir: '))
x = 0
while x <= fim:
    if x % 2 != 0:
        print(x)
    x += 1

# Exercício 5.5

fim = 30
x = 3
while x <= 30:
    print(x)
    x += 3

# Exercício 5.6 

num = int(input('Tabuada do: '))
multiplicador = 1
while multiplicador <= 10:
    resultado = num * multiplicador
    print(f'{multiplicador} X {num} = {resultado}')
    multiplicador += 1    

# Exercício 5.7

num = int(input('Tabuada do: '))
inicio = int(input('Por qual número gostaria de começar? '))
fim = int(input('E qual será o último número? '))
while inicio <= fim:
    resultado = num * inicio
    print(f'{inicio} X {num} = {resultado}')
    inicio += 1


# Exercício 5.8

num1 = int(input('Diga um número: '))
num2 = int(input('Agora diga outro para multiplicá-lo: '))
x = 1
resultado = 0
while x <= num2:
    resultado += num1
    x += 1
print(resultado)

# Exercício 5.9

n1 = int(input('Diga um número: '))
n2 = int(input('Agora diga outro para dividí-lo: '))
quociente = 0  
x = n1
while x >= n2:
    x -= n2
    quociente += 1
resto = x
print(f'{n1} / {n2} = { quociente}, resta {resto}')

# Exercício 5.10

pontos = 0
questão = 1
while questão <= 3:
    resposta = input(f'Resposta da questão {questão}: ')
    if questão == 1 and (resposta == 'b' or resposta == 'B'):
        pontos += 1
    if questão == 2 and (resposta == 'a' or resposta == 'A'):
        pontos += 1
    if questão == 3 and (resposta == 'd' or resposta == 'D'):
        pontos += 1
    questão += 1
print(f'O aluno fez {pontos} ponto(s)')

# Exercício 5.11

deposito = float(input('Qual é o depósito inicial? '))
juros = float(input('Qual é a taxa de juros da poupança? '))
mes = 1
saldo = deposito
while mes <= 24:
    saldo += (saldo * (juros / 100))
    print(f'O saldo do {mes}º mês é R${saldo:5.2f}')
    mes += 1    
print(f'O total obtido com o juros foi de R${saldo - deposito:5.2f}')

# Exercício 5.12

deposito = float(input('Qual é o depósito inicial? '))
juros = float(input('Qual é a taxa de juros da poupança? '))
mes = 1
deposito_mensal = float(input('Qual será o depósito mensal? '))
saldo = deposito
while mes <= 24:
    saldo += (saldo * (juros / 100)) + deposito_mensal
    print(f'O saldo do {mes}º mês é R${saldo:5.2f}')
    mes += 1    
print(f'O total obtido com o juros foi de R${saldo - deposito:5.2f}')

# Exercício 5.13

divida = float(input('Qual o valor inicial da dívida? '))
juros_mensal = float(input('Qual o juros mensal da dívida? '))
mensal = float(input('Qual valor mensal será pago? '))
# printar o numero de meses até acabar a divida e o total pago e o total de juros pago

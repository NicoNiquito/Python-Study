# Capítulo 4: Condições

# Exercício 4.2
velocidade = int(input('Qual a velocidade do seu carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f'Você foi multado em R${multa}')

# Exercício 4.3
n1 = int(input('Me diga o 1º número'))
n2 = int(input('Me diga o 2º número'))
n3 = int(input('Me diga o 3º número'))
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O maior número é o {maior} e o menor é {menor}')

# Exercício 4.4
salário = float(input('Qual o seu salário? '))
if salário > 1250.00:
    aumento = salário * 0.10
    salário = salário + aumento
if salário <= 1250.00:
    aumento = salário * 0.15
    salário = salário + aumento
print(f'O aumento foi de R${aumento}. Seu salário agora é de R${salário}')

# Exercício 4.5
idade = int(input('Qual a idade do seu carro? '))
if idade <= 3:
    print('Seu carro é novo')
else:
    print('Seu carro é velho')

# Exercício 4.6
dist = float(input('Quantos Km você deseja percorrer? '))
if dist > 200:
    preço = dist * 0.45
    print(f'A viagem vai custar R${preço:5.2f}')
else:
    preço = dist * 0.50
    print(f'A viagem vai custar R${preço:5.2f}')

# Exercício 4.8
n1 = int(input('Diga um número inteiro: '))
n2 = int(input('Diga outro: '))
sinal = input('Qual operação você gostaria de realizar? Digite \'+\', \'-\', \'*\' ou \'/\': ')
if sinal == '+':
    soma = n1 + n2
    print(f'O resultado é {soma}')
elif sinal == '-':
    subtração = n1 - n2
    print(f'O resultado é {subtração}')
elif sinal == '*':
    multiplicação = n1 * n2
    print(f'O resultado é {multiplicação}')
elif sinal == '/':
    divisão = n1 / n2
    print(f'O resultado é {divisão}')
else:
    print('Você não digitou valores válidos.')

# Exercício 4.9
print('Aprova empréstimo para compra de casa se a parcela for menos que 30% do salário')
preço = float(input('Qual o valor da casa?'))
salário = float(input('De quanto é o seu salário? R$'))
anos = int(input('Quantos anos para pagar a casa?'))
prestação = preço / anos
limite = salário * 0.30
if prestação > limite:
    print('Você não está apto para a compra da casa.')
else:
    print('Você está apto para a compra da casa')

# Exercício 4.10
print('Vamos calcular o preço da energia')
inst = input('Qual o tipo de instalação? Digite \'R\' para residências, \'C\' para comércios e \'I\' para indústrias: ').lower()
kwh = float(input('Qual a quantidade de kWh consumida? '))
if inst == 'r':
    if kwh <= 500:
        preço = 0.40
    else:
        preço = 0.65
elif inst == 'c':
    if kwh <= 1000:
        preço = 0.55
    else: 
        preço = 0.60
elif inst == 'i':
    if kwh <= 5000:
        preço = 0.55
    else:
        preço = 0.60
print(f'A conta será de R${kwh * preço:5.2f}')

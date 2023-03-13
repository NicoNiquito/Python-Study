# O livro em questão é o ''Introdução à programação com Python'', por Nilo Ney.
# Estou utilizando o livro pra rever todo conteúdo visto até agora e me aprofundar ainda mais.
# Dito isto, os primeiros estudos com o livro serão "apenas" revisões. :)

# Exercício 3.7
n1 = int(input('Me diga um número inteiro: '))
n2 = int(input('Agora diga outro: '))
print(n1 + n2)

# Exercício 3.8
metros = float(input('Me diga um valor em metros: '))
milímestros = metros * 1000
print(f'{metros} metros equivalem à {milímestros} milímetros.')

# Exercício 3.9
dias = int(input('Me dê um número de dias: '))
horas = int(input('Me dê uma número de horas: '))
minutos = int(input('Me dê um número de minutos: '))
segundos = int(input('Me dê um número de segundos: '))

segundos += dias * 86400
segundos += horas * 3600
segundos += minutos * 60
print(f'Isso equivale à {segundos} segundos.')

# Exercício 3.10
print('Vamos calcular o aumento de um salário')
salário = float(input('Qual é o salário atual? R$'))
porcentagem = float(input('Qual a porcentagem do aumento? '))
aumento = salário * porcentagem / 100
novo_salário = salário + aumento
print(f'Com um aumento de R${aumento:5.2f}, o novo salário é R${novo_salário:5.2f}')

# Exercício 3.11
print('Vamos calcular o valor de um desconto')
preço = float(input('Qual é o preço do produto? R$'))
porcentagem = float(input('Qual é a porcentagem do desconto? '))
desconto = preço * porcentagem / 100
valor_a_pagar = preço - desconto
print(f'Com um desconto de R${desconto:5.2f}, o valor a pagar é R${valor_a_pagar:5.2f}')

# Exercício 3.12
print('Vamos calcular o tempo de uma viagem')
dist = float(input('Me diga a distância a ser percorrida em Km: '))
vel = float(input('Me diga a velocidade média em Km/h: '))
tempo = vel / dist
print(f'A viagem demoraria {tempo} horas.')

# Exercício 3.13
print('Vamos converter uma temperatura de °C para °F')
c = float(input('Me diga a temperatura em °C: '))
f = 9 * c / 5 + 32
print(f'A temperatura é {f}°F')

# Exercício 3.14
print('Vamos calcular o preço a pagar pelo aluguel do carro. (R$60 por dia + R$0,15 por Km rodado.)')
km_percorridos = float(input('Quantos km foram percorridos? '))
dias = float(input('Por quantos dias o carro foi alugado? '))
preço = dias * 60 + km_percorridos * 0.15
print(f'O preço a se pagar é de R${preço}')

# Exercício 3.15
print('Vamos calcular a redução do tempo de vida causada pelo cigarro. (1 ciggaro = - 10 minutos)')
cigarros_por_dia = int(input('Quantos cigarros você fuma por dia? '))
anos = int(input('A quantos anos você fuma? '))
anos = anos * 365
minutos_por_dia = cigarros_por_dia * 10
minutos_por_ano = anos * minutos_por_dia
dias_perdidos = int(minutos_por_ano / 1440)
print(f'Fumando {cigarros_por_dia} cigarros por dia ao longo de {anos} anos, perde-se {dias_perdidos} dias de vida.')



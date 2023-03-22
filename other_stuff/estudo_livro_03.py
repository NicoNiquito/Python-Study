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

dívida = float(input("Dívida: "))
taxa = float(input("Juros (Ex.: 3 para 3%): "))
pagamento = float(input("Pagamento mensal:"))
mês = 1
if (dívida * (taxa/100) > pagamento):
    print("Sua dívida não será paga nunca, pois os juros são superiores ao pagamento mensal.")
else:
    saldo = dívida
    juros_pago = 0
    while saldo > pagamento:
        juros = saldo * taxa / 100
        saldo = saldo + juros - pagamento
        juros_pago = juros_pago + juros
        print(f"Saldo da dívida no mês {mês} é de R${saldo:6.2f}.")
        mês = mês + 1
    print(f"Para pagar uma dívida de R${dívida:8.2f}, a {taxa:5.2f} % de juros,")
    print(f"você precisará de {mês - 1} meses, pagando um total de R${juros_pago:8.2f} de juros.")
    print(f"No último mês, você teria um saldo residual de R${saldo:8.2f} a pagar.")

# Exercício 5.14

numeros = 0
soma = 0
media_aritmetica = 0
while True:
    n = int(input('Digite um número inteiro ou digite 0 para finalizar: '))
    if n == 0:
        break
    numeros += 1
    soma += n
media_aritmetica = soma / numeros
print(f'Você digitou {numeros} números, sendo que a soma deles é {soma} e a sua média aritmética é {media_aritmetica}')

# Exercício 5.15

p1 = 0
p2 = 0
p3 = 0
p5 = 0
p9 = 0

while True:
    codigo = int(input('Digite o código do produto(1, 2, 3, 5, 9) ou 0 para sair: '))
    if codigo == 0:
        break
    else:
        if codigo == 1:
            quantidade = int(input('Quantas unidades desse produto foram compradas? '))
            p1 += quantidade
        elif codigo == 2:
            quantidade = int(input('Quantas unidades desse produto foram compradas? '))
            p2 += quantidade
        elif codigo == 3:
            quantidade = int(input('Quantas unidades desse produto foram compradas? '))
            p3 += quantidade
        elif codigo == 5:
            quantidade = int(input('Quantas unidades desse produto foram compradas? '))
            p5 += quantidade
        elif codigo == 9:
            quantidade = int(input('Quantas unidades desse produto foram compradas? '))
            p9 += quantidade
        else:
            print('Código inválido.')

valor_total = p1 * 0.50 + p2 * 1.00 + p3 * 4.00 + p5 * 7.00 + p9 * 8.00
print(f'O total a ser pago é R${valor_total}')

# Exercício 5.16

valor = int(input('Digite o valor a pagar: '))
cedulas = 0
atual = 50
a_pagar = valor
while True:
    if atual <= a_pagar:
        a_pagar -= atual
        cedulas += 1
    else:
        print(f'{cedulas} cédula(s) de R${atual}')
        if a_pagar == 0:
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0

# Exercício 5.18

valor = int(input('Digite o valor a pagar: '))
cedulas = 0
atual = 100
a_pagar = valor
while True:
    if atual <= a_pagar:
        a_pagar -= atual
        cedulas += 1
    else:
        print(f'{cedulas} cédula(s) de R${atual}')
        if a_pagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0

# Exercício 5.19

valor = float(input('Digite o valor a pagar: '))
cedulas = 0
atual = 100
a_pagar = valor
while True:
    if atual <= a_pagar:
        a_pagar -= atual
        cedulas += 1
    else:
        print(f'{cedulas} cédula(s) de R${atual}')
        if a_pagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01   
        cedulas = 0

# Exercício 5.21

while True:
    valor = int(input('Digite o valor a pagar: '))
    if valor == 0:
        break
    cedulas = 0
    atual = 50
    a_pagar = valor
    while True:
        if atual <= a_pagar:
            a_pagar -= atual
            cedulas += 1
        else:
            print(f'{cedulas} cédula(s) de R${atual}')
            if a_pagar == 0:
                break
            if atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            cedulas = 0

# Exercício 5.22

while True:
    operacao = int(input('Escolha uma operação:\n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Sair'))
    if operacao == 5:
        break
    elif operacao >= 1 and operacao <= 5:
        num = int(input('Tabuada do: '))
        x = 1
        while x <= 10:
            if operacao == 1:
                print(f'{x} + {num} = {x + num}')
            elif operacao == 2:
                print(f'{num} - {x} = {num - x}')
            elif operacao == 3:
                print(f'{x} X {num} = {x * num}')
            elif operacao == 4:
                print(f'{num} / {x} = {num / x:5.2f}')
            x += 1
    else:
        print('Operação inválida. ')

# Exercício 5.23

num = int(input('Diga um número: '))
if num < 0:
    print('Digite um número válido.')
elif num == 0 or num == 2:
    print('Não é primo, mas é um caso especial.')
else:
    if num == 2:
        print('2 é Primo')
    elif num % 2 == 0:
        print('Não é primo, pois é divisível por 2 e não é 2')
    else:
        x = 3
        while x < num:
            if num % x == 0:
                break
            x += 2
        if x == num:
            print(f'{num} é primo')
        else:
            print(f'{num} não é primo, pq pode ser dividido por {x}')


# Exercício 5.24

n = int(input('Diga um número: '))
x = 1
if n < 0:
    print('Número inválido.')
else:
    print('2')
    w = 3
    while x < n:
        u = 3
        while u < w:
            if w % u == 0:
                break
            u += 2
        if u == w:
            print(w)
            x += 1
        w += 2

# Exercício 5.25
print('Obtendo raíz quadrada pelo método de Newton')

n = float(input('Raíz quadrada do número: '))
b = 2
while abs(n - (b ** 2)) > 0.0001:
    p = (b + (n / b)) / 2
    b = p
print(f'Aproximadamente {p: 5.2f}')

# Ps: essa função abs() retorna o valor absoluto de um número. "Valor absoluto nada mais é do que a distância entre um número e 0 na reta numérica."

# Exercício 5.26


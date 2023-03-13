#   ->Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

x = input('Digite algo')
print('O tipo primitivo é:', type(x))
print('É formado por letra(s)?', x.isalpha())
print('É formado por número(s)?', x.isnumeric())
print('É formado por letras e números?', x.isalnum())
print('Está em maiúsculo?', x.isupper())
print('Está em minúsculo?', x.islower())
print('Está capitalizado?', x.istitle())

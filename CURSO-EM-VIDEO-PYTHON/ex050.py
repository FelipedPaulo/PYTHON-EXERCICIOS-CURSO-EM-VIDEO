'''Exercício Python 50: Desenvolva um programa que leia seis números
inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.'''
soma = 0
cont = 0
for c in range(1,7):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
if cont == 1:
    print(f'Você digitou {cont} número PAR e a soma é {soma}')
#melhorei colocando singular, 2022/04/23
else:
    print(f'Você digitou {cont} números PARES e a soma é {soma}')

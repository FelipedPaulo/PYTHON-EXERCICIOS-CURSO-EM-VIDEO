'''Exercício Python 52: Faça um programa que
leia um número inteiro e diga se ele é ou não um número primo.'''

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num +1):
    if num % c == 0:
        print('\033[34m', end=" ")
        tot += 1
    else:
        print('\033[33m', end=" ")
    print(f'{c}', end=" ")
print(f'\n\033[m O número {num} foi dividido {tot} vezes.')
if tot == 2:
    print('\033[m Por isso ele É PRIMO!')
else:
    print('\033[m Por isso ele NÃO é PRIMO!')




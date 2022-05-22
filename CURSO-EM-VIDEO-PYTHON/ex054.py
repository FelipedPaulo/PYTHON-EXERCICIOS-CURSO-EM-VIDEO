'''Exercício Python 54: Crie um programa que leia o ano de nascimento
de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores.'''
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input(f'Digite o ano que a {pess}ª pessoa nasceu: '))
    idade = atual - nasc
    if idade <= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Tivemos um total de \033[33m {totmaior} \033[m pessoas maiores de idade')
print(f'Tivemos um total de \033[31m {totmenor} \033[m pessoas menores de idade')
'''Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro
termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while.'''

termo = int(input('Digite o termo da PA: '))
razao = int(input('Digite a Razão da PA: '))
cont = 0
while cont < 10:
    termo += razao
    cont += 1
    print(termo, end='')
    print('--> ' if cont < 10 else '', end='')
'''Exercício Python 079: Crie um programa onde o usuário
possa digitar vários valores numéricos e cadastre-os em
uma lista. Caso o número já exista lá dentro, ele não
será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.'''

num = []
while True:
    n = int(input('Digite um número para adicionar a lista: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não irei adicionar...')
    r = str(input('Deseja continuar ? [S/N]')).upper().strip()[0]
    if r in 'N':
        break
num.sort()
print(f'Você digitou {num}')

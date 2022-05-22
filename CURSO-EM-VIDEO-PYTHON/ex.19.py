'''import random
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('DIgite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')
ran = random(n1,n2,n3,n4)
print('O aluno sorteado foi'.format(ran))'''
'''Fiz igual igual está em cima, errei'''

import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

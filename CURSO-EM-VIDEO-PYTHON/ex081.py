'''Exercício Python 081: Crie um programa que vai ler vários
números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar ? [S/N]')).strip().upper()
    if resp in 'N':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos')
print(f'A lista em ordem decrescente é {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não foi encontrado na lista')
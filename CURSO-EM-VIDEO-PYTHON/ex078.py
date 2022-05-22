'''Exercício Python 078: Faça um programa que leia 5 valores
numéricos e guarde-os em uma lista. No final, mostre
qual foi o maior e o menor valor digitado e as
suas respectivas posições na lista.'''

listanum = []
mai = men = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um número para posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('*-*'*20)
print(f'Voê digitou os valores {listanum}')
print(f'O maior valor foi {mai}')
print(f'O menor valor foi {men}')
print('*-*'*20)
'''Exercício Python 084: Faça um programa que leia
nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

lista = []
dados = []
bigger = smaller = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite a peso: ')))
#    lista.append(dados[:]) ---> assim mostra q o menor peso é 0, fazer
# todo o tratamento e dps agregar na lista
    if len(lista) == 0: # se a lista ñ tem elementos, maior e menor será o mesmo.
        bigger = smaller = dados[1]
    else: #looping para substituir valores.
        if dados[1] > bigger:
            bigger = dados[1]
        if dados[1] < smaller:
            smaller = dados[1]
    lista.append(dados[:]) #colocando dados tratados na lista
    dados.clear() #limpando para colocar mais dados
    resp = str(input('Quer continuar ?: [S/N]')).strip().upper()
    if resp in 'N':
        break
print(lista)
print(f'O maior peso foi {bigger}Kg. que foi de', end='')
for p in lista:
    if p[1] == bigger:
        print(f' [{p[0]}]', end='')
print()
print(f'O menor peso foi de {smaller}.Kg que foi de', end='')
for p in lista:
    if p[1] == smaller:
        print(f' [{p[0]}]', end='')


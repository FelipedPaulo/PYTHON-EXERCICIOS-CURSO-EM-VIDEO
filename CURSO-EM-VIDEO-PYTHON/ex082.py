'''Exercício Python 082: Crie um programa que vai ler vários
números e colocar em uma lista. Depois disso, crie duas
listas extras que vão conter apenas os valores pares e
os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

listatot = []
listapar = []
listaimpar = []
while True:
    listatot.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja Continuar ? [S/N]')).upper().strip()
    if resp in 'N':
        break
for i, v in enumerate(listatot):
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)
print(f'A lista criada foi {listatot}')
print(f'Os pares da lista são {listapar}')
print(f'Os ímpares da lista são{listaimpar}')

'''Exercício Python 70: Crie um programa que leia o nome e o preço de
 vários produtos. O programa deverá perguntar se o usuário vai
 continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''
tot = maisqmil = maisbarato = cont = 0
barato =' '
print('-*-'*15)
print('{:-^40}'.format('Loja Super Baratão'))
print('-*-'*15)
while True:
    produto = str(input('Qual produto você comprou ?: ')).upper().strip()
    preço = float(input('Qual o Valor ?: R$'))
    continuar = ' '
    cont += 1
    tot += preço
    if preço > 1000:
        maisqmil += 1
    if cont == 1 or preço < maisbarato:
        maisbarato = preço
        barato = produto
    while continuar not in 'SN':
      continuar = str(input('Deseja continuar ? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print('-*-'*15)
print(f'O total da compra é R$ {tot}')
print(f'Você comprou {maisqmil} produtos que custam mais que R$ 1.000,00')
print(f'O produto mais barato foi o {barato} e o valor dele foi R$ {maisbarato:.2f}')
print('-*-'*15)




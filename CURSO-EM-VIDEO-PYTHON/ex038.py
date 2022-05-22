'''Exercício Python 038: Escreva um programa que leia dois números
inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais'''

cores = {'limpa':'\033[m','azul':'\033[34m','vermelho':'\033[31m','amarelo':'\033[33m'}
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
if n1 > n2:
    print(f'O {cores["azul"]} PRIMEIRO{cores["limpa"]} valor é maior')
elif n1 < n2:
    print(f'O {cores["amarelo"]}SEGUNDO{cores["limpa"]} valor é maior')
elif n1 == n2:
    print(f'Os {cores["vermelho"]}VALORES{cores["limpa"]} são iguais')

'''Exercício Python 65: Crie um programa que leia vários números
inteiros pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor valores
lidos. O programa deve perguntar ao usuário se ele quer ou
não continuar a digitar valores.'''

num = cont = soma = media = maior = menor = 0
continuar = 's'
while continuar in 'sS':
    digite = int(input('Digite um número: '))
    continuar = str(input('Você quer continuar ? [S/N] ')).upper().strip()[0]
    cont += 1
    soma += digite
    if cont == 1:
        maior = menor = digite
    else:
        if digite > maior:
            maior = digite
        if num < menor:
            menor = digite
media = (soma / cont)
print(f'Você digitou {cont} números e a média foi {media:.2f}')
print(f'O maior foi {maior} e o menor foi {menor}')
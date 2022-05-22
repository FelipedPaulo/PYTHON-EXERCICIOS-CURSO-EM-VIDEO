'''Exercício Python 51: Desenvolva um programa que leia o
primeiro termo e a razão de uma PA. No final,
mostre os 10 primeiros termos dessa progressão.'''

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a RAZÃO: '))
décimo = primeiro + (10 - 1) * razao
for c in range(primeiro,décimo + razao,razao):
    print(f'{c}', end=" ")
print('ACABOU')

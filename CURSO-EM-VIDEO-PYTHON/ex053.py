'''Exercício Python 53: Crie um programa que leia uma frase
qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
 Exemplos de palíndromos:'''
frase = str(input('Digite uma palavra: ')).strip().upper()
separa = frase.split()
junta = ''.join(separa)
inverso = ''
for letra in range(len(junta) -1, -1, -1):
    inverso += junta[letra]
print(f'O inverso de {junta} é {inverso}')
if junta == inverso:
    print('Temos um PALÍNDROMO')
else:
    print('A frase digitada NÃO é um Palíndromo')



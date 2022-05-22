'''import random
from time import sleep
n1 = int(input('Pensei em um número de 0 a 5, tenta adivinhar qual é: '))
lista = [0, 1, 2, 3, 4, 5]
n2 = random.choice(lista)
print('Processando Resposta...')
sleep(3)
print(f'O número que pensei foi {n2}')
if n1 == n2:
    print('Parabéns, você adivinhou o número que pensei')
else:
    print('Suas habilidades de adivinha não são tão boas, melhor fazer outra coisa')'''

#testando outro método
from time import sleep
from random import randint
computador = randint(0, 5)
print('Pensei em um número entre 0 e 5 tente adivinhar.')
escolha = int(input('Digite sua escolha: '))
print('Processando escolha...')
sleep(1)
if escolha == computador:
    print(f'Parabéns eu pensei em {computador} e você adivinhou')
else:
    print(f'Eu pensei em {computador} Você errou, tente novamente...')



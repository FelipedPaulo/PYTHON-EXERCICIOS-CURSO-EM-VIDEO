'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde
o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar
até acertar, mostrando no final quantos
palpites foram necessários para vencer.'''

from random import randint
escolha = randint(0,10)
jogador = int(input('Pensei em um número entre 0 a 10, tente adivinhar: '))
tentativa = 1
while jogador != escolha:
    jogador = int(input('VocÊ errou, tente novamente: '))
    tentativa += 1
    if jogador == escolha:
        acertou = True
    else:
        if jogador < escolha:
            print('Mais...tente novamente')
        elif jogador > escolha:
            print('Menos...tente novamente')
print(f'Parabéns você acertou em {tentativa} tentativas.')

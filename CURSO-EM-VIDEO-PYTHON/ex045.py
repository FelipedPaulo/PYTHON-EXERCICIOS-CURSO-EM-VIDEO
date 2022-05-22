from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Escola uma das opções
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=-' * 20)
print(f'O Note jogou {itens[computador]}')
print(f'Você jogou {itens[jogador]}')
print('-=-' * 20)
if computador == 0: #note jogou PEDRA
    if jogador == 0:
        print(f'O note jogou {itens[computador]} e você jogou {itens[jogador]}: Jogo empatado')
    elif jogador ==1:
        print(f'O note jogou {itens[computador]} e você jogou {itens[jogador]}: Você Venceu!')
    elif jogador == 2:
        print(f'O note jogou {itens[computador]} e você jogou {itens[jogador]}: Você Perdeu!')
    else:
        print('Jogada Inválida, Tente Novamente.')

elif computador == 1: #note jogou PAPEL
    if jogador == 0:
        print(f'O note jogou {itens[computador]} você jogou {itens[jogador]}: Você Perdeu!')
    elif jogador == 1:
        print(f'O note jogou {itens[computador]} você jogou {itens[jogador]}: Jogo Empatado!')
    elif jogador == 2:
        print(f'O note jogou {itens[computador]} você jogou {itens[jogador]}: Você Venceu!')
    else:
        print('Jogada Inválida, Tente Novamente.')

elif computador == 2: #note jogou TESOURA
    if jogador == 0:
        print(f'O note jogou {itens[computador]} você jogou {itens[jogador]}: Você Venceu!')
    elif jogador == 1:
        print(f'O note jogou {itens[computador]} você jogou {itens[jogador]}: Você Perdeu')
    elif jogador == 2:
        print(f'O note jogou {itens[computador]} você jogou {itens[jogador]}: Jogo Empatado')

    else:
        print('Jogada Inválida, Tente Novamente.')




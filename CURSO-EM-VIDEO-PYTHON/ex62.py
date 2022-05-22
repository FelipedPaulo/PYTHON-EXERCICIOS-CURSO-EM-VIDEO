'''Exercício Python 62: Melhore o DESAFIO 61, perguntando para o
usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
'''
print('=-='*3,'Gerador de PA','=-='*3)
termo = int(input('Digite o Termo: '))
razao = int(input('Digite a Razão: '))
cont = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont < total:
        termo += razao
        cont += 1
        print(termo, end='')
        print(' -> ' if cont < total else'', end='')
    print('\nPausa')
    mais = int(input('Quantos termos deseja ver a mais?: '))
print(f'Progressão finalizada com {total} de termos')


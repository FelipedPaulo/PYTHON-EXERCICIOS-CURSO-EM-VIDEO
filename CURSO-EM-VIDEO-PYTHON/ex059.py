'''Exercício Python 059:
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print(str('''    [1] Somar
    [2] Multiplicar
    [3] Maior 
    [4] Novos números
    [5] Sair do programa'''))
    opcao = int(input('>>> Digite sua opção: '))
    if opcao == 1:
        print(f'A soma dos valores é: {(v1 + v2)}')
    elif opcao == 2:
        print(f'A multiplicação dos valores é: {(v1 * v2)}')
    elif opcao == 3:
        if v1 > v2:
            print(f'O maior valor é: {v1}')
        else:
            print(f'O maior valor é: {v2}')
    elif opcao == 4:
        v1 = int(input('Digite o primeiro valor: '))
        v2 = int(input('Digite o segundo valo: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida: ')
    print('=-='* 10)
print('Fim do programa, volte sempre')

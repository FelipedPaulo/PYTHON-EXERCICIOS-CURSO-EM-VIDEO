'''Exercício Python 72: Crie um programa que tenha uma
dupla totalmente preenchida com uma contagem por
extenso, de zero até vinte. Seu programa deverá ler
um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    while True:
        núm = int(input('Digite um número entre 0 e 20: '))
        if 0 <= núm <= 20:
           break
        print('Tente Novamente...')
    print(f'Você digitou {cont[núm]}')
    resp = str(input('Você deseja continuar ? [S/N]')).strip().upper()
    if resp == 'N':
        break
print('Fim do programa...')


'''
jml1640
há 2 anos
Utilizando a solução do Prof. Guanabara, eu acrescentei um "Deseja continuar?[S/N]" conforme foi sugerido pelo próprio professor.
Para fazer isso, eu aninhei todo o loop infinito (while True) do código dentro de outro loop infinito.
Ficou assim:

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <=20:
            break
        print('Número inválido. ', end='')
    print(f'O número digitado foi {cont[num]}.')
    print(' ')
    resp = str(input('Deseja continuar?[S/N]: ')).upper().strip()
    if resp == 'N':
        break
print('-' * 40)
print('PROGRAMA ENCERRADO')'''
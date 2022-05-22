'''Exercício Python 077: Crie um programa que tenha uma tupla
com várias palavras (não usar acentos). Depois disso,
você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ('aprender', 'testando', 'python',
            'abraçar', 'guerra')
for p in palavras:
    print(f'\nA palavra {p.upper()}', end=' ')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end='')

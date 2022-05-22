'''frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} neste nome'.format(frase.upper().count('A')))
print('A posição da primeira letra A é {}'.format(frase.index('A') + 1))
# print('A última posição que a letra A aparece é {}'.format(nome.rindex('A'))) #
print(f'A última posição q a letra A aparece é {frase.rfind("A")}')
# fazer uso das aspas duplas quando usar o comando f desse jeito #
'''

frase = str(input('Digite uma frase: ')).upper().strip().replace(" ","")
print(f'A letra aparece {frase.count("A")} nessa frase')
print(f'O primeiro "A" aparece na posição {frase.find("A")+1}')
print(f'O ultimo "A" aparece na posição {frase.rfind("A")+1}')

'''nome = str(input('Digite seu nome: ')).strip().upper()
if nome == 'Felipe'.upper():
    print('Que nome lindo você tem')
else:
    print('Que nome normal')
print(f'Bom dia, {nome}')
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi: {m}')
if m >= 6.0:
    print('Você passou, PARABÉNS!')
else:
    print('Você repetiu, estude mais ano que vem!')

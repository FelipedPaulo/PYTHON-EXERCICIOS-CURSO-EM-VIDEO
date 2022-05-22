'''nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva ? {} \n'.format('silva' in nome.lower()))'''

n = str(input('Digite seu nome: ')).strip()
print(f'Seu nome tem SIlva ? {"silva" in n.lower()}')

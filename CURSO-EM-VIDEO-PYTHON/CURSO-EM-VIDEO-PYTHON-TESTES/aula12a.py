nome = str(input('Dgite seu nome: ')).strip().upper()
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m'}
if nome == 'FELIPE':
    print('Que nome bonito você tem {}{}{}'.format(cores['azul'],nome,cores['limpa']))
elif nome == 'LUCAS' or 'RENATA':
    print(f"Você tem um nome normal {cores['amarelo']}{nome}{cores['limpa']}")
else:
    print(f'Olá {nome}')

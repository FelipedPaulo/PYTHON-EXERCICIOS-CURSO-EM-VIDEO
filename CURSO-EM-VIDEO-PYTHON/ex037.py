'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''
#cores \033[0;33;44m   primeiro \33 dps estilo 0 dps cor do texto ;33
#por ultimo o background ;44m no final sempre coloca m.
cores = {'limpa':'\033[m','azul':'\033[34m','amarelo':'\033[33m','roxo':'\033[35m',
         'vermelho':'\033[31m'}
num = int(input('Digite um número inteiro: '))
print(('''Escolha uma das bases de conversão: 
[1] Converta para BINÁRIO
[2] Converta para OCTAL
[3] Converta para HEXADECIMAL'''))
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('O valor {} em BINÁRIO é {}{}{}'.format(num,cores['azul'],bin(num)[2:],cores['limpa']))
elif opcao == 2:
    print('O valor {} em OCTAL é {}{}{}'.format(num,cores['amarelo'],oct(num)[2:],cores['limpa']))
elif opcao == 3:
    print('O valor {} em HEXADECIMAL é {}{}{}'.format(num,cores['roxo'],hex(num)[2:],cores['limpa']))
else:
    print(f'{cores["vermelho"]}Opção inválida!, tente novamente{cores["limpa"]}')

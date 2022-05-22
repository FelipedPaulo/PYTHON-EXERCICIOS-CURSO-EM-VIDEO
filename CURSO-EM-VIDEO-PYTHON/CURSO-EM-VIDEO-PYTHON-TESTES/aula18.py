'''Nessa aula, vamos aprender o que são LISTAS
e como utilizar listas em Python. As listas
são variáveis compostas que permitem armazenar
vários valores em uma mesma estrutura,
acessíveis por chaves individuais.'''
#01 exemplo
'''teste = []
teste.append('Felipe')
teste.append('26')
galera = list()
galera.append(teste[:]) # [:] para fazer uma cópia, se não usar, ele duplica.
teste[0] = 'Rex'
teste[1] = '50'
galera.append(teste[:])
print(teste)'''

'''#02 exemplo Lista dentro de lista
galera = [['felipe', 26], ['isabel', 22], ['nina', 6]]
for p in galera:
    print(p[0])
    print(f'{p[0]} tem {p[1]} idade')
print(galera[0][0])'''

#03 exemplo
galera = []
dado = list()
totmai = 0
totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear() #para limpar antes de fazer a próxima
#continuando para analisar os dados
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
print(galera)
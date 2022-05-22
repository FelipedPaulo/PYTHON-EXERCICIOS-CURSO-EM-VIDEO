'''Exercício Python 083: Crie um programa onde o
usuário digite uma expressão qualquer que use
parênteses. Seu aplicativo deverá analisar se
a expressão passada está com os parênteses
abertos e fechados na ordem correta.'''

expr = str(input('Digite uma expressão'))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
    else:
        pilha.append(')')
        break
if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está invalida')

'''
Ricardo Carvalho
há 3 anos
Eu fiz através do comando 'count' que você já ensinou, acho que ficou melhor!! fiz assim:


expr = str(input('Digite a expressão: '))
if exp.count('(') == exp.count(')'):
    print('Sua expressão é válida!!')
else:
    print('Sua expressão não é válida')'''
'''Exercício Python 69: Crie um programa que leia
a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o
usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''
M = F20 = P18 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    resp = ' '
    if idade < 20 and sexo == 'F':
        F20 += 1
    if sexo == 'M':
        M += 1
    if idade > 18:
        P18 += 1
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('Programa Finalizado')
print(f'Foram cadastrados:\n {P18} maiores de 18 anos')
print(f'Um total de {M} Homens')
print(f'Um total de {F20} mulheres menores de 20 anos')



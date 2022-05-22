num = int(input('Digite um número: '))
print('Analisando o número {}'.format(num))
#poderia ser n1 = num % 10 o resultado seria o msm#
n1 = num // 1 % 10
n2 = num // 10 % 10
n3 = num // 100 % 10
n4 = num // 1000 % 10
print('Unidade {}'.format(n1))
print('Dezena {}'.format(n2))
print('Centena {}'.format(n3))
print('Milhar {}'.format(n4))
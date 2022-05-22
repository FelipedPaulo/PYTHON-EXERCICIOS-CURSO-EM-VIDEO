'''Exercício Python 36: Escreva um programa para aprovar
o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e
em quantos anos ele vai pagar. A prestação mensal não
pode exceder 30% do salário ou então o empréstimo será negado.'''

cores = {'limpa':'\033[m','azul':'\033[34m','vermelho':'\033[31m'}
vcasa = float(input('Digite o valor da casa:R$ '))
s = float(input('Digite o valor do seu salário:R$ '))
anos = float(input('Digite em quantos anos deseja pagar:R$ '))
prest = (vcasa / (anos * 12))
print(f'A prestação será de R${prest:.2f}')
if prest >= s * (30 / 100):
    print('A prestação da casa excede 30% do seu salário', end='')
    print('\n{}Não é possível fazer o emprestimo{}'.format(cores['vermelho'],cores['limpa']))
else:
    print('{}Parabéns, você conseguiu o emprestimo{}'.format(cores['azul'],cores['limpa']))

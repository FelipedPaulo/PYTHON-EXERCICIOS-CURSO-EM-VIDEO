'''Exercício Python 44: Elabore um programa que calcule o
valor a ser pago por um produto, considerando o seu preço
normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros'''

print('{:=^40}'.format (' Lojas Hatata '))
preco = float(input('Digite o valor da compra:R$ '))
opcao = int(input('''Digite a forma de pagamento:
[1] À Vista, Cheque/Dinheiro
[2] À Vista no Cartão
[3] Cartão até 2x
[4] Cartão 3x ou mais\n'''))
if opcao == 1:
    total = preco - (preco * (10 / 100))
    print(f'O valor a pagar com 10% de desconto é {total}')
elif opcao == 2:
    total = preco - (preco * (5 / 100))
    print(f'O valor a pagar com 5% de desconto é {total}')
elif opcao == 3:
    v = int(input('Irá dividir em quantas vezes: '))
    if v == "1":
        print(f'O valor é {preco}')
    else:
        print(f'O valor das parcelas sera 2x de {preco/2} ')
elif opcao == 4:
    v2 = float(input('Irá dividir em quantas vezes: '))
    total = preco + (preco + (20 / 100))
    print(f'O valor de cada parcela será de {total / v2} e o valor total é de {total}')

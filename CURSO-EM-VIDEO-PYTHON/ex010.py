n = float(input('Digite quanto de dinheiro você tem R$'))
s = (n/3.27)
print('Considerando da cotação do Dólar em R$ 3.27', end= " ")
print('Você poderia comprar U${:.2f} dólares'.format(s))
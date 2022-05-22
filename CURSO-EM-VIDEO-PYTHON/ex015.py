d = int(input('Quantos dias o carro ficou alugado?'))
km = float(input('Quantos km percorreu?'))
dias = d * 60
kmr = km * 0.15
s = float(dias + kmr)
print('O Total a pagar é de R$ {:.2f}'.format(s))


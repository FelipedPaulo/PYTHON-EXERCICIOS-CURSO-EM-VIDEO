#calc de salario de funcionarios, quem ganha até R$1250, ganha 15% de aumento
#quem ganha acima de 1250 ganha 10% de aumento.
s = float(input('Digite o sálario do funcionário:R$ '))
if s <= 1250:
    aumento = (s * (15/100)) + s
else:
    aumento = (s * (10/100)) + s
print(f'O novo salário deste funcionário será de {aumento}')

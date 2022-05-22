#Programa que leia 3 seguimentos e diga se é possível criar um triângulo
a = float(input('Digite primeiro valor: '))
b = float(input('Didigite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))
if (a+b)>c and (a+c)>b and (b+c)>a:
    print(f'É possível formar um triângulo com as medidas{a,b,c}')
else:
    print(f'Não é possível formar um triângulo com as medidas {a,b,c}')

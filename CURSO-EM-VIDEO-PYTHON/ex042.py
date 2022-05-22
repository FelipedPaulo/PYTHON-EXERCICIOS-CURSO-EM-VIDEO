a = float(input('Digite primeiro valor: '))
b = float(input('Didigite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))
if (a+b)>c and (a+c)>b and (b+c)>a:
    print(f'É possível formar um triângulo com as medidas{a,b,c}')
    if a == b == c:
        print('EQUILÁERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print(f'Não é possível formar um triângulo com as medidas {a,b,c}')

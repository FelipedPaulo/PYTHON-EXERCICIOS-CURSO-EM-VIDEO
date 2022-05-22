v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
v3 = float(input('Digite o terceiro valor: '))
#verificando qual é o menor
#escolhendo um como menor, no caso V1, elimina a necessidade de outro if.
menor = v1
if v2<v1 and v2<v3:
    menor = v2
if v3<v2 and v3<v2:
    menor = v3
print(f'O menor valor é {menor}')
#verificando o maior valor
maior = v1
if v2>v1 and v2>v3:
    maior = v2
if v3>v1 and v3>v2:
    maior = v3
print(f'O maior valor é {maior}')

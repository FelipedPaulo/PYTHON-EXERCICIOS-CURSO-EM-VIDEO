'''Exercício Python 43: Desenvolva uma lógica que leia o peso e a
altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida'''

peso = float(input('Qual é o seu peso:(Kg)'))
alt = float(input('Qual é a sua altura:(metros) '))
calc = peso/(alt**2)
imc = calc
if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f}: Abaixo do peso')
elif imc > 18.5 and imc < 24.9:
    print(f'Seu IMC é de {imc:.2f}: Peso normal')
elif imc > 25 and imc < 29.9:
    print(f'Seu IMC é de {imc:.2f}: Sobrepeso')
elif imc > 30 and imc < 34.9:
    print(f'Seu IMC é de {imc:.2f}: Obesidade Grau 1')
elif imc > 35 and imc < 39.9:
    print(f'Seu IMC é de {imc:.2f}: Obesidade Grau 2')
else:
    print(f'Seu IMC é de {imc:.2f}: Obesidade Móbida')

#viagem até 200km cobrar R$0,50 por KM
#viagem acima de 200km cobrar R$0,45 por KM
dist = float(input('Digite a distância em KM: '))
if dist <= 200:
    print('O valor da sua passagem é de R$',dist*0.50)
else:
    print('O valor da passagem é de R$', dist*0.45)

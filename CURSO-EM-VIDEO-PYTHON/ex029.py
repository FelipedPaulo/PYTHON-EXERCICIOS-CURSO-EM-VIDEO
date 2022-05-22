'''km = float(input('Digite a que velocidade você estava: '))
if km <= 80:
    print('Você estava dentro da velocidade permitida, não fez mais que a obrigação \n parabéns!')
else:
    multa = (km - 80) * 7
    kmulta = km - 80
    print(f'Você utrapassou em {kmulta} a velocidade, sua multa é de R$ {multa}')
'''
#condição simples só utilisa um if sem o else.
#Obs: ao usar o f ao invés do format, a conf de casas fica assim {dados:.2f}
#Excemplo R${multa:.2f}.
km = int(input('Digite a velocidade que vc estava dirigindo Km:'))
if km > 80:
    print('MULTADO! você excedeu o limite permitido de 80Km/h')
    kmulta = (km - 80)
    multa = kmulta * 7
    print(f'Você ultrapassou {kmulta}Km/h do permitido. O valor da multa a pagar é R${multa:.2f}!')
print('Digija com cuidado e tenha um bom dia!')
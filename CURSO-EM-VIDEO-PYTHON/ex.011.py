n = float(input('Digite em metros a altura da parede: '))
n2 = float(input('Agora digire em metros a largura da parede: '))
s = n*n2
s1 = s/2
print('Considereando que cada litro de tinta pinta uma área de 2m²',end='')
print('\n para uma parede com área de {}m²'.format(s),end='')
print('\n Você vai precisar de {} litros \n de tinta para pintar toda a parede'.format(s1))


n = float(input('Escreva a medida em metros:'))
km = n/1000
hm = n/100
dam = n/10
dm = n*10
cm = n * 100
mm = n * 1000
print('A medida {:.2f} equivale a'.format(n),end='\n')
print('{}km'. format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{}dm'.format(dm))
print('{}cm'.format(cm))
print('{}mm'.format(mm))

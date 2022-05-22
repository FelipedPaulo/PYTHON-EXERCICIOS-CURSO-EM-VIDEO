'''import math
n = float(input('Digite o primeiro cateto: '))
n1 = float(input('Digite o segundo cateto: '))
h2 = float(n**2 + n1**2)
h = math.sqrt(h2)
print('Para os catetos {:.2f} e {:.2f} a hipotenusa será {:.2f}'.format(n,n1,h))
'''

from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente:'))
hi = hypot(co,ca)
print('Para os catetos {} e {} a hipotenusa será {:.2f}'.format(co,ca,hi))

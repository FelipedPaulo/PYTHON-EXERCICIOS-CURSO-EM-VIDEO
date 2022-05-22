'''import math
an = float(input('Digite o ângulo: '))
sen = math.sin(an)
cos = math.cos(an)
hi = math.tan(an)
print('Para o ângulo de {} o seno será {:.2f}'.format(an,sen),end='\n')
print('Para o ângulo de {} o cosseno será {:.2f}'.format(an,cos))
print('Para o ângulo de {} a tangente será {:.2f}'.format(an,hi))'''

import math
an = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('Para o ângulo {} o seno é {:.2f}'.format(an,sen))
print('Para o ângulo {} o cosseno é {:.2f}'.format(an,cos))
print('Para o ângulo {} sua tangente é {:.2f}'.format(an,tan))

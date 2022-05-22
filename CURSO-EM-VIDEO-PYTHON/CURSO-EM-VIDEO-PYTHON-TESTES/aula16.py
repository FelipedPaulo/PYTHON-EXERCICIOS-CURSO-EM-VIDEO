'''Nessa aula, vamos aprender o que são TUPLAS
e como utilizar tuplas em Python.
As tuplas são variáveis compostas e imutáveis
que permitem armazenar vários valores em uma
mesma estrutura, acessíveis por chaves individuais.'''
'''Tuplas São Imutáveis'''

#lanche = ('hambúrguer', 'suco', 'pizza', 'pudim')
#for cont in range(0, len(lanche)):
 #   print(lanche[cont])

#for pos, comida in enumerate(lanche):
#    print(f'Eu vou comer {comida} na posição {pos}')
#for comida in lanche:
   # print(f'Eu vou comer {comida}')
#print(len(lanche))
#print(lanche[3])


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.count(5)) #aparece 2 vezes o 5
print(c.index(8)) # a posição do 8 é 1
print(c.index(5,1)) #mostre o 5 começando da posição 1
'''Exercício Python 73: Crie uma tupla preenchida com
os 20 primeiros colocados da Tabela do Campeonato
Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

#criando a TUPLA (td Tupla é imutável)
times = ('Santos', 'Atlético-MG', 'Corinthians', 'Cuiabá', 'Internacional',
         'Avaí', 'Bragantino','Palmeiras', 'Flamengo', 'Coritiba',
         'São Paulo', 'Botafogo', 'Fluminense', 'América-MG'
         'Ceará SC', 'Athletico-PR', 'Atlético-GO',
         'Goiás', 'Juventude', 'Fortaleza')
print(times)
print(f'Os 5 primeiros são: {times[0:5]}')
print(f'Os últimos 4 colocados são: {times[-4:]}')
print(f'Os times em ordem alfabética: {sorted(times)}')
print(f'O São Paulo está na {times.index("São Paulo")}ª posição ')
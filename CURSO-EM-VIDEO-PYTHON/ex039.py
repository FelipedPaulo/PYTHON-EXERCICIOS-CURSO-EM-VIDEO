'''Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

import datetime
cores = {'limpa':'\033[m','azul':'\033[34m','amarelo':'\033[33m'}
data = int(input("Digite o ano de nasceimento: "))
idade = (datetime.date.today().year - data)
alistamento = data + 18
if idade == 18:
    print(f'Você tem {cores["amarelo"]}{idade}{cores["limpa"]} anos e deve se alistar esse ano')
elif idade > 18:
    print(f'Você tem {cores["amarelo"]}{idade}{cores["limpa"]} anos, seu ano de alistamento foi {alistamento}')
elif idade < 18:
    print(f'Você tem {cores["azul"]}{idade}{cores["limpa"]} anos e deve se alistar no ano {alistamento}')

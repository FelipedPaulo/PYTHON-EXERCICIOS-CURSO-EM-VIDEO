from datetime import date
nasc = int(input('Digite o ano de nascimento: '))
colors = {'clean':'\033[m','red':'\033[31m','green':'\033[32m',
          'yellow':'\033[33m','blue':'\033[34m','purple':'\033[35m'}
idade = date.today().year - nasc
if idade <= 9:
    print(f'Você tem {colors["red"]}{idade}{colors["clean"]} e sua categoria é'
          f' {colors["red"]}MIRIM{colors["clean"]}')
elif idade > 9 and idade < 15:
    print(f'Sua idade é {colors["green"]}{idade}{colors["clean"]} e sua categotia é '
          f'{colors["green"]}INFANTIL{colors["clean"]}')
elif idade > 14 and idade < 20:
    print(f'Sua idade é {colors["yellow"]}{idade}{colors["clean"]} e sua categoria é '
          f'{colors["yellow"]}JUNIOR{colors["clean"]}')
elif idade > 19 and idade < 26:
    print(f'Sua idade é {colors["blue"]}{idade}{colors["clean"]} e sua categoria é '
          f'{colors["blue"]}SÊNIOR{colors["clean"]}')
elif idade > 25:
    print(f'Sua idade é {colors["purple"]}{idade}{colors["clean"]} e sua categoria é '
          f'{colors["purple"]}MASTER{colors["clean"]}')


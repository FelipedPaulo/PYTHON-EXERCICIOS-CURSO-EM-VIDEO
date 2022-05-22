colors = {'clean':'\033[m','blue':'\033[34m','red':'\033[31m'}
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) /2
if media < 5:
    print(f'A média da escola é 7 você tirou {media}')
    print(f'você está {colors["red"]}REPORVADO{colors["clean"]}')
elif media >= 5 and media < 7:
    print(f'A média da escola é 7 você tirou {media}')
    print(f'você está em {colors["blue"]}RECUPERAÇÃO{colors["clean"]}')
elif media >= 7:
    print(f'A média da escola é 7 você tirou {media}')
    print(f'Você está {colors["blue"]}APROVADO{colors["clean"]}')




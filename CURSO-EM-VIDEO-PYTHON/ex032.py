from datetime import date
ano = int(input('Digite o ano para saber se ele é Bissexto, digite 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
#se o ano é divisivel por 4 ou seja, se o resto da divisao por 4 é 0.
# diferente de 0 ou !=.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é Bissexto')
else:
    print(f'O ano {ano} não é Bissexto')

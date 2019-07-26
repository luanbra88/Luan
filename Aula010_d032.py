'''FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE
SE ELE É BISSEXTO'''

year = int(input('\033[7;30mDigite um ano com 4 digitos(Ex: 1998): \033[m'))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('O ano \033[44m{}\033[m é um ano bissexto!'.format(year))
else:
    print('O ano \033[34m{}\033[m não é bissexto!'.format(year))

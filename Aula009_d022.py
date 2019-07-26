'''CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA
PESSOA E MOSTRE:

O NOME COM TODAS AS LETRAS MAIUSCULAS

O NOME COM TODAS LETRAS MINUSCULAS

QUANTAS LETRAS AO TODO(SEM CONSIDERAR ESPAÇOS)

QUANTAS LETRAS TEM O PRIMEIRO NOME
'''

nome = str(input('\033[41mDigite o nome completo: \033[m'))

n1 = nome.upper()
n2 = nome.lower()
n3 = len(nome) - nome.count(' ')
n4 = nome.split()
n4Count = len(n4[0])

print('\033[42mO nome {} \033[m\n\033[46mcom todas as letras maiusculas sera: {}\033[m'
      '\n\033[43mcom todas as letras minusculas sera: {}\033[m'
      '\n\033[44mtem {} letras(sem considerar espaços) e \033[m'
      '\n\033[45mo primeiro nome tem {} letras\033[m'
      ''.format(nome, n1, n2, n3, n4Count))



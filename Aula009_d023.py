'''FAÇA UM PROGRAMA QUE LEIA UM NUMERO DE 0 A 9999
E MOSTRE NA TELA CADA UM DOS DIGITOS SEPARADOS.
EX: DIGITE UM NUMERO:  1834

UNIDADE: 4
DEZENA:3
CENTENA:8
MILHAR:1
'''

#TENTATIVA COM INT
number = int(input('\033[47mDigite um numero entre 0 e 9999: \033[m'))

unidade = number // 1 % 10
dezena = number // 10 % 10
centena = number // 100 % 10
milhar = number // 1000 % 10

print('\033[31mPara o numero: {}\033[m'
      '\n\033[32mUnidade: {}\033[m'
      '\n\033[33mDezena: {}\033[m'
      '\n\033[34mCentena: {}\033[m'
      '\n\033[35mMilhar: {}\033[m'
      .format(number, unidade, dezena, centena, milhar)
      )

#TENTATIVA COM STRING
# number = str(input('Digite um número: '))
#
# print('Unidade: {} '
#       '\nDezena: {} '
#       '\nCentena: {}'
#       '\nMilhar: {}'
#       .format(number[3], number[2], number[1], number[0])
#       )
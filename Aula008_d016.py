'''CRIE UM PROGRAMA QUE LEIA UM NÚMERO QULAQUER PELO TECLADO E
MOSTRE NA TELA A SUA POSIÇÃO INTEIRA

EX: 6.127 TEM A PARTE INTEIRA 6

OLHAR CLASSE MATH
'''
import math

n1 = float(input('Digite um numero(Use ponto ao invés de virgula)'))

inteiro = math.floor(n1)
#DICIONARIO DE CORES
cores = {
    'limpa':'\033[m',
    'vermelho':'\033[31m',
    'roxo':'\033[35m'
}
print('O valor inteiro do número {}{}{} é {}{}{}'
      .format(cores['vermelho'], n1, cores['limpa'],
              cores['roxo'], inteiro, cores['limpa'])
      )





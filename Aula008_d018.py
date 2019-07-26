'''FAÇA UM PROGRAMA QUE LEIA UM ÃNGULO QUALQUER E MOSTRE
NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE ÂNGULO

CARREGAR BIBLIOTECA ADEQUADA
'''

import math

anngulo = float(input('Digite um ângulo em graus(use ponto ao invés de virgula): '))



seno = math.sin(math.radians(anngulo))

cosseno = math.cos(math.radians(anngulo))

tangente = math.tan(math.radians(anngulo))

#DICIONARIO DE CORES
cores = {
      'limpa':'\033[m',
      'vermelho':'\033[36;41m',
      'amarelo':'\033[33m',
      'azul':'\033[44m',
      'branco':'\033[7;30;47m'
}
print('Para o angulo {}{}{} temos o valor de '
      'seno {}{:.2f}{}, '
      'o cosseno {}{:.2f}{} e '
      'tangente {}{:.2f}{}!'
      .format(cores['vermelho'], anngulo, cores['limpa'],
              cores['amarelo'], seno, cores['limpa'],
              cores['azul'], cosseno, cores['limpa'],
              cores['branco'], tangente, cores['limpa'])
      )

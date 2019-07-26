'''FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO
ADJACENTE DE UM TRIANGULO RETANGULO, CALCULE E MOSTRE O COMPRIMENTO
DA HIPOTENUSA

USAR MÓDULOS
'''

from math import hypot

catOposto = float(input('Digite o tamanho do cateto oposto: '))
catAdja = float(input('Digite o tamanho do cateto adjacente: '))

cHipotenusa = hypot(catAdja, catOposto)
#DICIONARIO DE CORES
cores = {
      'limpa':'\033[m',
      'verde':'\033[1;32m',
      'amarelo':'\033[4;43m',
      'ciano':'\033[1;47m'
}

print('o tamanho da hipotenusa do triangulo com cateto adjacente {}{}{}'
      ' e cateto oposto {}{}{} é: {}{}{}'
      .format(cores['verde'], catAdja, cores['limpa'],
              cores['amarelo'], catOposto, cores['limpa'],
              cores['ciano'], cHipotenusa, cores['limpa'])
      )

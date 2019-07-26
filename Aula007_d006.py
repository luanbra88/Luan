'''CRIE UM ALGORITMO QUE LEIA UM NÚMERO E MOSTRE
SEU DOBRO, TRIPLO E RAIZ QUADRADA.'''

n1 = float(input('Digite um número: '))

dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)
#DICIONARIO DE CORES
cores = {
    'limpa':'\033[m',
    'UndVerdeAzul':'\033[4;32;44m',
    'NegCiano':'\033[7;46m',
    'NegAmareloCinza':'\033[1;33;47m',
    'VermelhoCiano':'\033[31;46m'
}

print('O dobro de {}{}{} é {}{}{}, o triplo é {}{}{} e a raiz quadrada é {}{}{}'
      .format(cores['UndVerdeAzul'],n1,cores['limpa'],
              cores['NegCiano'],dobro,cores['limpa'],
              cores['NegAmareloCinza'],triplo,cores['limpa'],
              cores['VermelhoCiano'],raiz,cores['limpa'])
      )

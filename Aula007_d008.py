'''ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA
CONVERTIDO EM CENTIMETROS E MILIMETROS'''

medida = float(input('Digite a medida obtida em metros: '))

centimetros = medida * 100
milimetros = medida * 1000

#DICIONARIO DE CORES
cores = {
    'limpa':'\033[m',
    'Vermelho':'\033[31;43m',
    'Roxo':'\033[1;35;46m',
    'Cinza':'\033[4;37;40m'
}

print('A medida de {}{}{} metros obtida '
      'vale {}{}{} centimetros '
      'e {}{}{} milimetros!'
      .format(cores['Vermelho'], medida,cores['limpa'],
              cores['Roxo'], centimetros, cores['limpa'],
              cores['Cinza'], milimetros, cores['limpa'])
      )

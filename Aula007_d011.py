'''FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA
PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA
NECESSÁRIA PARA PINTA-LA, SABENDO QUE CADA LITRO DE TINTA,
PINTA UMA ÁREA DE 2M²'''

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parecde: '))

area = larg * alt
tinta = area/2
#DICIONARIO DE CORES
cores = {
    'limpa':'\033[m',
    'InvVermelho':'\033[7;41m',
    'BoldBrancoCinza':'\033[1;30;47m'
}

print('Para uma área de {}{}{} metros quadrados, '
      'será necessário {}{}{} litros de tinta'
      .format(cores['InvVermelho'], area, cores['limpa'],
              cores['BoldBrancoCinza'], tinta, cores['limpa'])
      )


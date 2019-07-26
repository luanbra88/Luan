'''CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA
TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR
U$1,00 = R$3,27'''

real = float(input('Quanto dinheiro você tem na carteira em reais(R$)?'))

dolares = real/3.27

#DICIONARIO DE CORE
cores = {
    'limpa':'\033[m',
    'RoxoBranco':'\033[35;40m',
    'VerdeCinza':'\033[32;44m'
}
print('Você tem R${}{:.2f}{} reais na carteira, isso vale US${}{:.2f}{} '
      'dólares que você pode comprar'
      .format(cores['RoxoBranco'], real, cores['limpa'],
              cores['VerdeCinza'], dolares, cores['limpa'])
      )

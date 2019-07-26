'''FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE
SEU NOVO PREÇO, COM 5% DE DESCONTO'''

prod = float(input('Digite o valor do produto: '))

desconto = prod * 0.95

#DICIONARIO DE CORES
cores = {
    'limpa':'\033[m',
    'BoldRoxoVerde':'\033[1;35;42m',
    'UndCianoCinza':'\033[4;36;47m'
}

print('O produto custava originalmente {}R${:.2f}{} e '
      'após o desconto irá custar {}R${:.2f}{}'
      .format(cores['BoldRoxoVerde'], prod, cores['limpa'],
              cores['UndCianoCinza'], desconto, cores['limpa'])
      )

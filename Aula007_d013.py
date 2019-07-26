'''FAÇA UM ALGROTIMO QUE LEIA O SALÁRIO DE UM FUNCIONARIO
E MOSTRE SEU NOVO SALÁRIO, COM 15% DE AUMENTO'''

salario =  float(input('Entre com o salário do funcionário'))

aumento = salario * 1.15
#DICIONARIO DE CORES
cores = {
    'limpa':'\033[m',
    'Azul':'\033[34;47m',
    'Ciano':'\033[30;47m'
}
print('O salario de {}R${:.2f}{}, '
      'após o reajuste será de {}R${:.2f}{}'
      .format(cores['Azul'], salario,cores['limpa'],
              cores['Ciano'], aumento, cores['limpa'])
      )
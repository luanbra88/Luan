'''DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS
DE UM ALUNO, CALCULE E MOSTRE SUA MÉDIA'''

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))

media = (n1+n2)/2
#DICIONARIO DE CORES
cores = {
    'limpa':'\033[m',
    'BrancoVerde':'\033[30;42m',
    'AzulVermelho':'\033[34;41m',
    'RoxoAmarelo':'\033[4;31;43m'
}

print('A primeira nota do aluno foi {}{}{}'
      .format(cores['BrancoVerde'], n1, cores['limpa'])
      )
print('A segunda nota do aluno foi {}{}{}'
      .format(cores['AzulVermelho'], n2, cores['limpa'])
      )
print("A mádia calculada do aluno foi: {}{}{}"
      .format(cores['RoxoAmarelo'], media, cores['limpa'])
      )

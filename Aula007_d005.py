'''FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA
SEU SUCESSOR E SEU ANTECESSOR'''

n1 = int(input("Digite um número: "))
ant = n1 - 1
suc = n1 + 1

#DICIONARIO DE CORES
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'NegRoxoCinza':'\033[1;37;43m'}

print('O antecessor de {}{}{} é {}{}{}'
      .format(cores['azul'],n1,cores['limpa'], cores['amarelo'],ant,cores['limpa']))
print('O sucessor de {}{}{} é {}{}{}'
      .format(cores['pretoebranco'],n1,cores['limpa'],cores['NegRoxoCinza'], suc, cores['limpa']))

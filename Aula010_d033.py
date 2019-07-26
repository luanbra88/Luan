'''FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL
É O MAIOR E QUAL É O MENOR'''

n1 = int(input('\033[45mDigite um número: \033[m'))
n2 = int(input('\033[33mDigite outro número: \033[m'))
n3 = int(input('\033[37mDigite um último número: \033[m'))
#MENOR
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#MAIOR
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor valor é \033[7;30;47m{}\033[m e o maior valor é \033[33m{}\033[m'
      .format(menor, maior)
      )

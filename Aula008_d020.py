'''O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM
DE APRESENTAÇÃO DE TRABALHOS DOS ALUNOS. FAÇA UM PROGRAMA
QUE LEIA O NOME DOS QUATRO ALUNOS E MOSTRE A ORDEM SORTEADA

'''

import random
#ou from random import shuffle

n1 = str(input('\033[31mPrimeiro Nome: \033[m'))
n2 = str(input('\033[32mSegundo Nome: \033[m'))
n3 = str(input('\033[33mTerceiro Nome: \033[m'))
n4 = str(input('\033[34mQuarto Nome: \033[m'))

lista = [n1, n2, n3, n4]

random.shuffle(lista)
#ou shuffle(lista)

print('\033[35mA ordem de apresentação será\033[m \n\033[36m{}\033[m'.format(lista))

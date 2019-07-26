'''UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA
APAGAR O QUADRO. FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO
O NOME DELES E ESCREVENDO O NOME DO ESCOLHIDO

USAR O MÓDULO RANDON PARA STRING
'''
import random

nom1 = str(input('\033[41mPrimeiro Aluno: \033[m'))
nom2 = str(input("\033[42mSegundo Aluno: \033[m"))
nom3 = str(input("\033[43mTerceiro Aluno: \033[m"))
nom4 = str(input("\033[44mQuarto Aluno: \033[m"))

lista = [nom1, nom2, nom3, nom4]

escolhido = random.choice(lista)

print('O Aluno escolhido foi: \033[45m{}\033[m'.format(escolhido))


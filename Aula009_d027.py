'''FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA
, MOSTRANDO EM SEGUIDA O PRIMEIRO E O ULTIMO NOME SEPARADAMENTE.
EX: ANA MARIA DE SOUZA
PRIMEIRO: ANA
ULTIMO: SOUZA'''

nome = str(input('\033[37mDigite seu nome completo: \033[m')).strip()

divide = nome.split()
tamDivide = len(divide)
print('\033[33mPara o nome {}\033[m'
      '\n\033[1;36mPrimeiro nome: {}\033[m'
      '\n\033[4;35mUltimo nome: {}\033[m'
      .format(nome, divide[0], divide[tamDivide-1])
      )


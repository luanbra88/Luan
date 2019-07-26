'''CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA
E DIGA SE ELA TEM "SILVA" NO NOME.'''

nome = str(input('\033[7;30mDigite seu nome completo: \033[m')).strip()

print('\033[31;47m','SILVA' in nome.upper(),'\033[m')

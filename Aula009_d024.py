'''CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE
E DIGA SE ELA COMEÇA COM O NOME "SANTO" '''

city = str(input('\033[35mDigite o nome da cidade: \033[m')).strip()

print('\033[45m',city[:5].upper() == 'SANTO','\033[m')




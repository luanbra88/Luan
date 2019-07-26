'''CRIE UM PROGRAMA QUE LEIA UM NÚMEREO INTEIRO
E MOSTRE NA TELA SE ELE É PAR OU IMPAR'''

number = int(input('\033[34mDigite um número: \033[m'))

if number % 2 == 0:
    print('O Número \033[43m{}\033[m é par!'.format(number))
else:
    print('O Número \033[36m{}\033[m é impar!'.format(number))
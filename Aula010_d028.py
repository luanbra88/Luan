'''ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR ´´´PENSAR´´
EM UM NUMERO INTEIRO ENTRE 0 E 5 E PEÇA PARA O USUARIO TENTAR DESCOBRIR
QUAL FOI NUMERO ESCOLHIDO PELO COMPUTADOR.

O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUARIO VENCEU
OU PERDEU'''
import random

guess = random.randint(0,5)
print('{}'.format(guess))

number = int(input('\033[31mDigite um número: \033[m'))

if guess == number:
    print('\033[32mParabens! Você acertou!\033[m')
else:
    print('\033[31mSinto muito! Você errou! \nTente novamente!\033[m')
'''ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO
QUE ELE FOI MULTADO.
A MULTA VAI CUSTAR R$7,00 POR CADA KM ACIMA DO
LIMITE'''

velocidade = float(input('Qual a velocidade do carro? \n'))

if velocidade >= 80:
    multa = (velocidade - 80) * 7.00
    print('Você foi multado em \033[41mR${}\033[m por estar \033[45m{}km/H\033[m acima do limite de velocidade!'
          .format(multa, velocidade-80)
          )
else:
    print("")
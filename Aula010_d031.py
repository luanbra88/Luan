'''DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTANCIA
DE UMA VIAGEM EM KM. CALCULE O PREÇO DA PASSAGEM, COBRANDO
R$0,50 POR KM PARA VIAGENS ATÉ 200KM E R$0,45 PARA
VIAGENS MAIS LONGAS'''

distancia = float(input('\033[mQual a distancia em Km até o destino? \n\033[m'))

if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print('o valor da passagem para uma viagem de \033[36m{}km\033[m '
      'será de \033[30;47mR${}\033[m'
      .format(distancia, passagem)
      )
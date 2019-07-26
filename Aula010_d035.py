'''DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO
DE TRÊS RETAS E DIGA AO USUARIO SE ELAS PODEM OU NÃO
FORMAR UM TRIÂNGULO

USAR PITAGORAS
'''
print('\033[34;47m-=\033[m'*20)
print('Analisador de Triângulos')
print('\033[32;41m-=\033[m'*20)

r1 = float(input('\033[42mDigite o tamanho da reta 1: \033[m'))
r2 = float(input('\033[41mDigite o tamanho da reta 2: \033[m'))
r3 = float(input('\033[45mDigite o tamanho da reta 3: \033[m'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[35mOs segmentos PODEM FORMAR um Triângulo!\033[m')
else:
    print('\033[36mOs segmentos NÃO PODEM FORMAR Triângulo!\033[m')


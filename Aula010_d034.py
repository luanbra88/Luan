'''ESCREVA UM PROGRAMA QUE PERGUNTE O SALARIO DE UM
FUNCIONÁRIO E CALCULE O VALOR DE SEU AUMENTO

PARA SALARIOS SUPERIORES A R$1250,00, CALCULE UM
AUMENTO DE 10%

PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%'''

salario = float(input('\033[36mDigite o salario \033[mR$'))

if salario <= 1250:
    salRecalc = salario * 1.15
else:
    salRecalc = salario * 1.10
print('O salario reajustado é \033[32mR${:.2f}\033[m'.format(salRecalc))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1+n2)/2
print('A sua media foi: {:.1f}'.format(m))

# if m >=6.0:
#     print('Sua media foi boa! APROVADO!')
# else:
#     print('Sua média foi ruim! REPROVADO!')
print('APROVADO!' if m >=6.0 else 'REPROVADO!')
print("--FIM--")


# nome = str(input('Qual é seu nome? '))
#
# if nome == 'Luan':
#     print('Acertou!')
# else:
#     print('Nome Comum!')
# print('Bom dia {}!'.format(nome))


# a = 3
# b = 5
# print('Os valores são \033[32;41m{}\033[m e \033[31;47m{}\033[m --FIM--'.format(a, b))

nome = 'Luan'

#DICIONÁRIO DE CORES
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('Ola! Muito prazer em te conhecer {}{}{}!!!'
      ''.format(cores['pretoebranco'], nome, cores['limpa']))
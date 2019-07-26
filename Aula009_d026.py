'''FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO
E MOSTRE:

QUANTAS VEZES APARECE A LETRA "A"

EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ

EM QUE POSIÇÃO ELA APARECE A ULTIMA VEZ'''

frase = str(input('\033[7;30mDigite um frase: \033[m')).strip()

print('Na frase \033[34m{}\033[m'
      '\na letra ´a´ aparece \033[35m{}\033[m vezes'
      '\nsendo \033[32m{}\033[m a primeira posição'
      '\ne \033[31m{}\033[m a ultima'
      .format(frase,
              frase.lower().count('a'),
              frase.lower().find('a') ,
              frase.lower().rfind('a')
              )
      )
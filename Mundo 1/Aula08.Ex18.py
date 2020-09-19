import math
ang= int(input('Digite o valor de um angulo:'))
rad= math.radians(ang)
cos= math.cos(rad)
sen = math.sin(rad)
tang= math.tan(rad)
#print('O valor do cos de \033[33m{}\033[m e igual a {}, o sen e igual a {} e a tang e igual a {}'.format(ang, cos, sen, tang))

cores = {'limpo':'\033[m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'lilas':'\033[1;35m',
         'ciano':'\033[1;36m',
         'negativo':'\033[1;47'}

print('O valor do cos de {}{}{} e igual a {}{}{}, o sen e igual a {}{}{} e a tang e igual a {}{}{}'
      .format(cores['vermelho'], ang,
              cores['limpo'], cores['verde'], cos,
              cores['limpo'], cores['amarelo'], sen,
              cores['limpo'], cores['ciano'],tang,
              cores['limpo']))
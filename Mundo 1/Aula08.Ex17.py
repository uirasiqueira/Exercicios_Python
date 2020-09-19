from math import hypot
x = int(input('Digite um valor do cat adjascente:'))
y = int(input('Digite um valor do cateto oposto:'))
h= int(hypot(x,y))
cores = {'nada':'\033[m',
         'Azul':'\033[34m',
         'Amarelo':'\033[31m',
         'Lilas':'\033[35m'}


print('O valor da {}hipotenusa{} e igual a {}{}{}'.format(cores['Azul'], cores['nada'], cores['Lilas'], h, cores['nada']))

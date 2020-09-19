#n= float(input('Digite um numero:'))
#inteiro = int(n)
#print('O numero \033[1;31m{}\033[m tem a sua parte inteira igual a \033[1;32m{}\033[m'.format(n, inteiro))

#ou

import math
n=float(input('Digite um numero:'))
inteiro= math.trunc(n)
print('O numero \033[4;36m{} tem a sua parte inteira igual a {}'.format(n, inteiro))

#ou

#n=float(input('Digite um numero:'))
#inteiro= math.floor(n)
#print('O numero {} tem a sua parte inteira igual a {}'.format(n, inteiro))

#Ou muitas outras formas. Podemos utilizar inteiro = math.trun ou math.ceil
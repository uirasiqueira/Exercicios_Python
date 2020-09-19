'''Crie um código em python que teste se o site Pudim
está acessível pelo computador usado.'''

'''import urllib.request
try:
    print(urllib.request.urlopen("http://pudim.com.br/").getcode())
except BaseException:
    print('\033[1;31mO sitel Pudim não está acessível no momento\033[m')'''


#Guanabara method

import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso')
    print(site.read())
'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados
aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse
dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
from operator import itemgetter

'''dados={'jogador1':randint(1,6),'jogador2':randint(1,6), 'jogador3':randint(1,6),
       'jogador4':randint(1,6)}

for c in dados:
    print(f'O {c} tirou {dados[c]}')
    sleep(0.5)

print('O ranking dos jogadores:')
for k, v in dados.items():
    print(k)
print(dados)
#não consegui ordenar'''

#Guanabara methods

jogo={'jogador1':randint(1,6),
      'jogador2':randint(1,6),
      'jogador3':randint(1,6),
      'jogador4':randint(1,6)}

ranking = []
print('Valores sprteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #selecionando o 1 ele irá ordenar de acordo com os valores se fosse 0 seria de acordo com as chaves
print(ranking)
print('    == Ranking dos jogadores ==')
for i, v in enumerate(ranking):
    print(f'     {i+1}ª lugar {v[0]} com {v[1]}.')
    sleep(1)


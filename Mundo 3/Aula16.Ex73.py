'''Cire uma tupla preenchida com os 20 primeiros colocados da tabela do Capeonato Bresileiro de Futebol,
na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados;
B) Os últimos 4 colocados;
C) Uma lista com os times em ordem alfabética;
D) Em que posição na tabela está o time da Chapecoense'''


cbf = ('Flamengo','Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo',
       'Internacional', 'Corinthians', 'Fortaleza-CE', 'Goiás', 'Bahia', 'Vasco da Gama',
       'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print('.-'*30)
print(f'{t}')
print('.-'*30)
posicao = ' '
cont = 0
print(':-'*35)
print(f'Os 5 primeiros colocados são:{cbf[0:5]}')
print(f'Os 4 últimos colocados foram:{cbf[16:21]}')
print(f'A ordem alfabética dos times são:{sorted(cbf)}')
#Guanabara method  print(f'O chapecoense está na {cbf.index("Chapecoense")+1}ª posição')
while posicao != 'Chapecoense':
       posicao = cbf[cont]
       cont+=1
print(f'A chapecoense está na posição {cont}')
print(':-'*35)
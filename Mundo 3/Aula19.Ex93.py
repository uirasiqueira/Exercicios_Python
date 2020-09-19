'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidde de gols feitos em cada partida. No final, tudo
isso será guardado em um dicionário, incluindo o total de gols feitos durante
o campeonato'''

tot=0
tabela={}
lista= []
tabela['nome']= str(input('Nome do jogador: '))
tabela['partidas']= int(input(f'Quantas partidas {tabela["nome"]} jogou? '))
for c in range (0, tabela['partidas']):
    jogos = int(input(f'Quantos gols na partida {c+1}?'))
    lista.append(jogos)
    tabela['gols']=lista
    tot+= jogos
tabela['total']=tot
print('=.'*30)
print(tabela)
print('=.'*30)
for k, v in tabela.items():
    print(f'O campo {k} tem o valor {v}')
print('=.'*30)
print(f'O jogador {tabela["nome"]} jogou {tabela["partidas"]} partidas.')
for c, v in enumerate(lista):
    print(f'Na partida {c+1}, fez {v} gols.')
print(f'Foi um total de {tot} gols')

#Guanabara methods
jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range (0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c}?')))
jogador['gols'] = partidas [:]
jogador['total'] = sum(partidas)
print('-='*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'         => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')
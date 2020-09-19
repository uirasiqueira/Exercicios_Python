'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente
'''


'''def ficha(lista):
    print('-.'* 15)
    nome = str(input('Nome do jogador: '))
    if nome == '':
        nome = '<deconhecido>'
    gols = str(input('Gols marcados: '))
    if gols == '':
        gols = '0'
    print('-.' * 15)
    list.append(nome)
    list.append(gols)
    return lista


list = []
reso = ficha(list)
print(f'O jogador {list[0]} fez {list[1]} gol(s) no campeonato!')'''

#Guanabra method

def ficha (jog ='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


#Programa principal

n= str(input('Nome do jogador: '))
g = str(input('Númeo de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g =0
if n.strip()=='':
    ficha(gol=g)
else:
    ficha(n,g)


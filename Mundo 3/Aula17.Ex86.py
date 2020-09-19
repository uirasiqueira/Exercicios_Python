'''Crie um programa que crie uma matriz de dimensão 3x3 e a preencha com um valores lidos pelo
 teclado:
#visualizar o exemplo no video
No final, mostre a matriz na tela, com a formatação correta.'''

'''lista = [[],[],[]]
for c in range (0,3):
    for v in range (0,3):
        lista[c].append(int(input(f'Digite um valor para posição [{c}, {v}]: ')))
for c in range(0,3):
    for v in range(0,3):
        print(f'[{lista[c][v]:^5}]', end='')
    print()'''

#guanabar method

matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):#for para linha
    for c in range (0,3): #for para coluna
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
print('-.'*30)
for l in range(0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()


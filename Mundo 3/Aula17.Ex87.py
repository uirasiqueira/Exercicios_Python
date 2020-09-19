'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados;
B) A soma dos valores da terceira coluna;
C) O maior valor da segunda linha.'''

lista = [[],[],[]]
spar=0
for c in range (0,3):
    for v in range (0,3):
        lista[c].append(int(input(f'Digite um valor para posição [{c}, {v}]: ')))
print('-.*'*15)
for c in range(0,3):
    for v in range(0,3):
        print(f'[{lista[c][v]:^5}]', end='')
        if lista[c][v]%2==0:
            spar+= lista[c][v]
    print()
print('-.*'*15)


print(f'A soma de todos os valores pares da matriz é {spar}')
print(f'A soma dos valores da 3ª coluna é {lista[0][2] + lista[1][2]+ lista[2][2]}')
print(f'O maior valor da 2ª linha é {max(lista[1])}')

#Guanabaras method


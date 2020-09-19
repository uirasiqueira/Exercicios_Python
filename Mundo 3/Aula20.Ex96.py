'''Faça um programa que tenha um função chamada área(), que receba as dimensões
de um terreno retangular (largura e comprimento) e mostre a área do terreno'''

#método igual do guanabara
def area(l,c):
    area = l*c
    print(f'A área do terreno de {l} x {c} será de {area}')


#programa principal
l = int(input('Largura (m): '))
c = int(input('Comprimento (m): '))
area(l,c)


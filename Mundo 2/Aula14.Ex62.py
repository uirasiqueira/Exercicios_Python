'''Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos'''

a1 = int(input('Digite o primeiro termo:'))
r = int(input('Digite a razao da PA:'))
c = 0
total = 0
mais = 10
while mais!=0:
    total = total + mais
    while c < total:
        print(a1)
        a1 = a1 + r
        c += 1
    print('PAUSA')
    mais= int(input('Quantos termos você ainda que ver mais? '))
print('FIM')
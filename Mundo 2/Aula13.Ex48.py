'''Faça um programa que calcule a soma entre todos os números ímpares
que são múltiplos de três e que se encontram no intervalo de 1 até 500'''

m = 0
n = 0
for c in range (1,501,2):
    if c%3==0:
        n+=c
    m+=1

print(f'\nA Soma dos \033[36m{m}\033[m numeros impares, que são multiplos de \033[1m3\033[m, entre o intervalo de 1 a 500, sera \033[31m{n}\033[m!')

#ou

'''soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c #a unica diferença desse condigo com o primeiro e a separação da fomula!!
print(f'A soma é: {soma}')

 #ou

r = 0
for c in range (3, 500, 3):
    if ( c % 2 ) == 1:
        r = (r + c)
    print (c)
print('a soma de todos os numeros impar mutiplicos de 3, de 1 a 500, é {}'.format(r))

#ou

m=0
for n in range (0,500,3):
    if n%3==0 and n%2==1:
        m+=n
        print(n)
print(m)'''

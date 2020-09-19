''' Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado

- Equilátero: todos os lados iguais;
- Isóceles: dois lados iguais;
- Escaleno: todos os lados diferentes'''

from time import sleep
print('-=-=-=-=-=- Analisador de triângulos -=-=-=-=-=-')
sleep(1)
r1= float(input('Digite o tamanho da 1° reta:'))
r2= float(input('Digite o tamanho da 2° reta:'))
r3= float(input('Digite o tamanho da 3° reta:'))
print('PROCESSING...')
sleep(3)
if r1< r2+r3 and r1> r2-r3 and r2< r1+r3 and r2>r1-r3 and r3< r1+r2 and r3>r1-r3:
    print(f'Os tamanhos \033[1;31m{r1}\033[m, \033[1;33m{r2}\033[m e \033[1;32m{r3}\033[m satisfazem as condições de um triângulo!')
    if r1==r2==r3:
        print('O triangulo e equilatero')
    elif r1==r2 or r1==r3 or r2==r3:
        print('O triangulo e Isoceles')
    else:
        print('O triangulo e Escaleno')

else:
    print('As retas \033[31m não\033[m satisfazem as condições de um triângulo')

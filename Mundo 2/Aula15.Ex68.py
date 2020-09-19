'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou o final do jogo.'''

print('=.' * 30)
print('                 Vamos jogar Par ou Ímpar?')
print('=.' * 30)

from random import randint
'''vencedor = 0
while True:
    n = str(input('impar ou par?'))
    valor =int(input('Jogue um valor entre 0 e 10: '))
    computador = randint(0, 11)
    soma = valor+computador
    resultado = soma%2 #essa variável pode ser suprimida. jogando a divisão do resto para o IF

    if resultado == 0: #Aqui
        if n == 'par':
            print(f'Você escolheu {n} e jogou o número {valor}. Eu joguei o número {computador}. Você ganhou')
        else:
            print(f'Você escolheu {n} e jogou o número {valor}. Eu joguei o número {computador}. Eu ganhei')
            break
    else:
        if n == 'impar':
            print(f'Você escolheu {n} e jogou o número {valor}. Eu joguei o número {computador}. Você ganhou')
        else:
            print(f'Você escolheu {n} e jogou o número {valor}. Eu joguei o número {computador}. Eu ganhei')
            break

    continuar = str(input('Quer continuar [S/N]:')).upper()
    if continuar == 'N':
        break
print('Fim')'''


#ou - Guanabara modes
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo= ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]#o strip serve para separar a frase. Mas nesse caso o usuário só irá digitar a primeira letra e não irá servir para nada (Mas no vídeo guanabara colocou e eu coloquei apenas para lembrar)
    print(f'Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR ')
    print(f'Você jogou {jogador} e o computador {computador}. Total foi de {total}', end=' ')
    if tipo == 'P':
        if total % 2 ==  0:
            print('VOCÊ VENCEU!')
            v+=1
        else:
            print('VOCÊ PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VÔCE VENCEU!')
            v+=1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...?')
print(f'GAME OVER! Você venceu {v} vezes.')
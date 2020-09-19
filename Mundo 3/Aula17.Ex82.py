'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares
digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

impar = []
par = []
lista = []
continuar=''
while continuar != 'N':
    num = int(input('Digite um número: '))
    lista.append(num)
    if num%2 == 0:
        par.append(num)
    else:
        impar.append(num)
    continuar = str(input('Quer continuar [S/N]: ')).upper()
print('~.'*20)
print('A lista completa é ', end='')
print(lista)
print('A lista com números ímpares é composta por ', end='')
print(impar)
print('A lista com números pares é composta por ', end='')
print(par)
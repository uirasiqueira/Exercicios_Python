'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.

Ex.

n= leiaInt('Digite um n')'''


'''def leiaInt(y):
    for cont in str(y):
        while y not in '1234567890':
            y = str(input('ERRO! Digite um número: '))
        else:
            return f'Você digitou o número {n}'


n = str(input('Digite um número: '))
print(leiaInt(n))
'''
#Guanabra methods

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


#Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

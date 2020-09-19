'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
da digitação de um número de tipo inválido. A proveite e crie também uma função
leiaFloat() com a mesma funcionalidade.'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interropida pelo usuário.')
        else:
            break
    return n


def leiaFloat(msg):
    n = 0
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO: por favor, digite um número real válido.\033[m')
        else:
            break
    return n

#Programa principal
n = leiaInt('Digite um número inteiro: ')
nf = leiaFloat('Digite um número real: ')
print(f'O valor do número inteiro foi {n} e o número real {nf}')
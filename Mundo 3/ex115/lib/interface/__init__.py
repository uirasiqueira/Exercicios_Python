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

def linha(tam=42):
    return '-' *tam


def cabeçalho(txt):
    print(linha())
    print(f'{txt:^42}') #ou {txt.center(42)}
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c+=1
    print(linha())
    opc = leiaInt('Sua Opção:')
    return opc
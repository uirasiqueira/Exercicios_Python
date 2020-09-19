def aumentar(preço=0, taxa=0, formato=False):
    '''
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preço: o preço que se quer reajustar
    :param taxa: qual é a porcentagem do aumento.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    '''
    resultado = (preço*taxa/100) + preço
    return resultado if formato is False else moeda(resultado)

def diminuir(preço =0, taxa=0, formato=False):
    resultado = preço - (preço*taxa/100)#Essa taxa é diferença, pois está em um scopo local
    return resultado if formato is False else moeda(resultado)

def dobro(preço = 0, formato=False):
    resultado = preço*2
    return resultado if not formato else moeda(resultado)

def metade(preço = 0, formato=False):
    resultado = preço/2
    return resultado if not formato else moeda(resultado)

def moeda(preço = 0, moeda = 'RS'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, preço)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-' * 30)

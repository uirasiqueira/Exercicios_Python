'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro
que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional)
 indicando se será mostrado ou não na tela
o processo de cálculo do factorial.'''

#Faltou o parâmetro show (Parte do código foi inserido pelo metodo de guanabara)
def fatorial(n, show=False):
    '''
    :param n: O número que será calculado.
    :return: O valor do fatorial de um número n.
    :param show: (opcional) Mostrar ou não a conta.
    '''
    y=n
    while y!=1:
        if show:
            print(f'{y} x ', end='')
            if y>1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        n = n*(y-1)
        y= y-1
    return n


help(fatorial)
print(fatorial(5, show=True))
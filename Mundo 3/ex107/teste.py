import moeda
'''#para que o nome moeda deixe de estar vermelho é necessário que ela esteja 
escrito junto com sua localização, referindo-se no código como: import ex107.moeda
'''
#ou
#from moeda import metade, dobro, aumentar #Essa opção não necessitar colocar o modulo antes da função

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')

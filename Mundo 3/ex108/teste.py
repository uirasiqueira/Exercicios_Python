from ex108 import moeda
#import moeda
'''#para que o nome moeda deixe de estar vermelho é necessário que ela esteja 
escrito junto com sua localização, referindo-se no código como: import ex107.moeda
'''
#ou
#from moeda import metade, dobro, aumentar #Essa opção não necessitar colocar o modulo antes da função

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')

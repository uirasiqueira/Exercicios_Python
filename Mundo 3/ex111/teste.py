from ex111.utilidadesCeV import moeda

#import moeda
'''#para que o nome moeda deixe de estar vermelho é necessário que ela esteja 
escrito junto com sua localização, referindo-se no código como: import ex107.moeda
'''
#ou
#from moeda import metade, dobro, aumentar #Essa opção não necessitar colocar o modulo antes da função

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 35, 22)

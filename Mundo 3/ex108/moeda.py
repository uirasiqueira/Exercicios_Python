def aumentar(preço=0, taxa=0):
    resultado = (preço*taxa/100) + preço
    return resultado

def diminuir(preço =0, taxa=0):
    resultado = preço - (preço*taxa/100)#Essa taxa é diferença, pois está em um scopo local
    return resultado

def dobro(preço = 0):
    resultado = preço*2
    return resultado

def metade(preço = 0):
    resultado = preço/2
    return resultado

def moeda(preço = 0, moeda = 'RS'):
    return f'{moeda}{preço:.2f}'.replace('.',',')
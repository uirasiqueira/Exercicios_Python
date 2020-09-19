def aumentar(preço=0, taxa=0, formato=False):
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
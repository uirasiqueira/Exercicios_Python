''' Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''


numeros = []
n= 0
for c in range (0,5):
    num = int(input('Digite um valor: '))
    if c==0 or num > numeros[-1]:#ou -> len(numeros)-1 representa o ultimo elemento da lista que é os números
        numeros.append(num)
        print('Adicionado ao final da lista')
    else:
        pos=0
        while pos < len(numeros):
            if num<= numeros[pos]:
                numeros.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos+=1
print('.-'*30)
print(f'Os valores digitados em ordem foram {numeros}')


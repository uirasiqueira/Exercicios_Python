'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em
uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas;
B) Uma listagem com as pessoas mais pesadas;
C) Uma listagem com as pessoas mais leves.'''

#Exercicio muuuuuuuuuuuuuuuuuuito importante!!
#Não consegui inserir o nome respectivo aos pesos
#Método a seguir fi o de Guanabara


maior = menor = 0
continuar= ''
temp = []
princ = []
while continuar != 'N':
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0: #princ na posição 0 será a primeira lista da lista [temp]
        maior = menor = temp[1] #temp[1] serã os números e não os nomes
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()#valor para não se repetir e lançar o output sem repetição
    continuar = str(input('Quer continuar [S/N]: ')).upper()


print('~'*30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {maior}kg. Peso de ', end= '')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end= ' ')
print()
print(f'O menor peso foi de {menor}kg. Peso de ', end= ' ')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end= '')
print()



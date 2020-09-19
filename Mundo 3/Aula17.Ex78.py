'''Faça um programa que leia 5 valores numéricos e guarde os em uma lista. No final, mostre qual foi o maior
e o menor valor digitado e as suas respectivas posiçõesna lista.'''

'''valores=[]
for c in range (0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}:')))#variável composta, pois será inserido 5 valores dentro do loop for

print(f' O maior valor digitado foi {max(valores)} na posição {valores.index(max(valores))}')
print(f' O menor valor digitado foi {min(valores)} na posição {valores.index(min(valores))}')'''


#ou Guanabara metodo

valores=[]
maior= 0
menor=0
for c in range (0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}:')))
    if c==0:
        maior=menor= valores[c]
    else:
        if valores[c]>maior:
            maior=valores[c]
        else:
            menor= valores[c]
print(f'O maior valor digitado foi {maior} na posição ', end='')
for i, v in enumerate(valores):
    if v==maior:
        print(f'{i}...', end='')
print()#Código para quebrar parágrafo e evitar que as frases fiquem uma do lado da outra
print(f'O menor valor digitado foi {menor} na posição', end='')
for i, v in enumerate(valores):
    if v==menor:
        print(f'{i}...', end='')
print()

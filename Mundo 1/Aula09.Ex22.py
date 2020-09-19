'''Crie um programa que leia o nome completa da pessoa:
1. O nome com todas as letras maiusculas
2. O nome com todas as letras minusculas
3. Quantas letras ao todo (sem considerar espaços)
3. Quantas letras tem o primeiro nome'''

nome = input('Digite seu nome completo:')
nome1 = nome.split()

#print (nome.upper())
#print(nome.lower())
#print(len(nome.replace(' ' , '')))
#print(len(nome1[0]))

#ou

print(nome.upper())
print(nome.lower())
print(len("".join(nome1))) #<<< diferença
print(len(nome1[0]))
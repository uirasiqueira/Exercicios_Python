''' Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.'''

'''princ = []
impar= []
par= []
for c in range (0,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
princ.append(sorted(impar[:]))
princ.append(sorted(par[:]))

print(f'Os valores pares digitados foram: {princ[0]}\n'
      f'Os valores ímpares digitados foram:  {princ[1]}')'''

#guanabara methods

núm = [[], []]
valor = 0
for c in range (1,8):
    valor = int(input(f'Digite o {c}ª valor: '))
    if valor %2 ==0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('~'*30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]}')
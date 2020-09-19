'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente'''

numeros =[]
cont= ''
while cont!= 'N':
    num = (input('Digite um valor: '))
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Você já adicionou esse número...Tente novamente!')
    cont = str(input('Quer continuar [S/N]: ')).upper()
print('~.'*40)
print(f' Você digitou os valores {sorted(numeros)}')

#ou Guanabara method



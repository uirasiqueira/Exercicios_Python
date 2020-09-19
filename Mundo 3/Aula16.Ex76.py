'''Crie um programa que tenha tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizandoos dados em forma tabular'''

print('~.' * 50)
print('{:^100}'.format('Bem Vindo ao Market Digital'))
print('~.' * 50)

'''print('Faça sua lista de compras e iremos organizá-la')
continuar = ''
while continuar != 'N':
    prod = str(input('Digite o produto que deseja adicionar:'))
    prec = float(input('Digite o preço do produto: '))
    continuar = str(input('Quer continuar [S/N]:')).upper()

tupla = (prod, prec)
print(tupla)'''

propre = (str(input('Digite o produto que deseja adicionar:')), float(input('Digite o preço do produto: ')),
          str(input('Digite o produto que deseja adicionar:')), float(input('Digite o preço do produto: ')),
          str(input('Digite o produto que deseja adicionar:')), float(input('Digite o preço do produto: ')),
          str(input('Digite o produto que deseja adicionar:')), float(input('Digite o preço do produto: ')),
          str(input('Digite o produto que deseja adicionar:')), float(input('Digite o preço do produto: ')),
          str(input('Digite o produto que deseja adicionar:')), float(input('Digite o preço do produto: ')),
          str(input('Digite o produto que deseja adicionar:')), float(input('Digite o preço do produto: ')))

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range (0, len(propre)):
    if pos % 2==0:                                      #todos os número na posição par dentro da tupla (No caso os produtos)
        print(f'{propre[pos]:.<30}', end='')                       #Os nomes alinhado a direito dentro de 30 caracteres
    else:
        print(f'R${propre[pos]:>7.2f}')
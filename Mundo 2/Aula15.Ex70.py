'''Crie um programa que leia o nome e o preço do produto. O programa deverá perguntar se o usuário vai continuar.
No final mostre:

A) Qual é o total gasto na compra;
B) Quantos produtos custam mais de R$1000;
C) Qual é o nome do produto mais barato.'''

total = numero = contador = menor = 0
parar = ''
barato= ' '
while True:
    produto = str(input('Qual o produto que vai comprar:'))
    preço = float(input('Qual o preço: '))
    contador+=1
    total += preço
    if preço > 1000:
        numero += 1
    if contador == 1 or preço < menor:
        menor = preço
        barato = produto
    parar = ' '
    while parar not in 'SN':
        parar = str(input('Quer continuar com suas compras[S/N]: ')).upper()
    if parar == 'N':
        break
print('~~~~~~ Fim do Pograma ~~~~~~')
print(f'O valor total da compra foi de {total}')
print(f'Foram comprados {numero} que custam mais de R$1000')
print(f'O produto mais barato custou {menor:.2f} e foi o {barato}.')

''' Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
de pagamento:

- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- em até 2x o cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

print('*.'*20)
print('        Supermercado Produto Bom')
print('*.'*20)
produto = float(input('Qual o preço do produto que deseja comprar?R$'))


print('''O pagamento pode ser feito em algumas opções:
[1] - A vista dinheiro/Cheque;')
[2] - A vista no cartão;')
[3] - Ate 2x no cartão;')
[4] - 3x ou mais no cartão''')
pagamento = int(input('Qual sera a sua forma de pagamento?'))
if pagamento ==1:
    print('Voce tera 10% de desconto. O produto saira por {} reais'.format(produto-(10/100*produto)))
elif pagamento ==2:
    print('Voce tera 5% de desconto. O produto saira por  {} reais'.format(produto-(5/100*produto)))
elif pagamento ==3:
    print('O preço do produto sera o valor normal. No valor de {} reais'.format(produto))
elif pagamento ==4:
    print('Sera comprado um juros de 20%. Ficando pelo valor de {} reais'.format((20/100*produto)+produto))


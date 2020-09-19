'''Adapte o código do desafio 107, criando uma função adicional
chamada moeda() que consiga mostrar os valores como um valor
monetário formatado.'''

from ex107 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p.__trunc__()},00 é R${moeda.metade(p).__trunc__()},00')
print(f'O dobro de R${p.__trunc__()},00 é R${moeda.dobro(p).__trunc__()},00')
print(f'Aumentando 10%, temos R${moeda.aumentar(p).__trunc__()},00')
print(f'Reduzindo 13%, temos R${moeda.diminuir(p).__trunc__()},00')
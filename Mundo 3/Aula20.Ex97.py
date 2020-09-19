'''Faça um programa que tenha  função chamada escreva(), que receba um texto qualquer
como parâmetro e mostre uma mensagem com tamanho adaptável.

Ex:
escreva('Olá, Mundo!')
Saída
~~~~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~~~~'''

def escreva(txt):
    print('-' * (len(txt)+5))
    print(f'  {txt}')
    print('-' * (len(txt)+5))


escreva('Ola, mundo')
escreva('Programador raiz')
escreva('Spacex')
escreva(' Eu quero cagar no alto da montanha azul')

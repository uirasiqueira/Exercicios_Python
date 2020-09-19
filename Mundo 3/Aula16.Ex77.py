'''Crie um programa que tenha uma tupla com várias palavras (não usa acentos). Depois disso,
você deve mostrar, para cada palavra, quais são as suas vogais.'''

conjunto = ('lutar', 'vida', 'festa', 'casa', 'avião', 'medico', 'cadeira', 'verbo')

for palavra in conjunto:
    print(f'\nNa palavra {palavra.upper()} temos:', end=' ')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')


import random

#lista = ['Lara', 'Carlos', 'Andreia', 'Beatriz']
#random.shuffle(lista)
#print('A ordem de apresentação sera {}'.format(lista))

#ou

a1 = input('Escolha o primeiro aluno:')
a2 = input('Escolha o segundo aluno:')
a3 = input('Escolha o terceiro aluno:')
a4 = input('Escolha o quarto aluno:')
lista = [a1,a2,a3,a4]
random.shuffle(lista)
print('A ordem de alunos a apresentar sera {}'.format(lista))


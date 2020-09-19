'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:

- Média abaixo de 5.0:
REPROVADO

- Média entre 5.0 e 6.9:
RECUPERAÇÃO

-Média 7.0 ou superior:
APROVADO'''

n1 = float(input('Qual foi a primeira nota do aluno?'))
n2 = float(input('Qual foi a segunda nota do aluno?'))
media = (n1+n2)/2

print(f'A sua media foi de {media}')

if media < 5:
    print('REPROVADO, estuda mais, lazarento!!')
elif 5 <= media <= 6.9:
    print('Você foi para a recuperação!')
elif media >= 7:
    print('Parabens, você foi aprovado!')
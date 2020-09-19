'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
de cada aluno individualmente. '''

'''continuar = ''
notas=[]
nome1 = []
boletim=[]
while continuar!='N':
    cont=0
    while True:
        nome = str(input('Nome do aluno: '))
        nome1.append(nome)
        nota1 = float(input('1ª nota do luno: '))
        notas.append(nota1)
        nota2 = float(input('2ª nota do aluno: '))
        notas.append(nota2)
        media = (nota1+nota2)/2
        nome1.append(media)
        cont+=1
        if cont == 1:
            break
    nome1.append(notas[:])
    notas.clear()#limpa os dados anteriores (que seriam repetidos) para inserção de novos
    boletim.append(nome1[:])
    nome1.clear()
    continuar = str(input('Quer continuar [S/N]: ')).upper()
print(boletim)'''
#Não consegui fazer o resto do código


#GUanabara methods

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2= float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(ficha)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')#numero formatada com 4 caracteres alinhado a esquerd, nome com 10 alinhado a esquerda e media com 8 carateresa alinhado a direita
print('-='*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <=len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
        #opc é o número do aluno
        # É o nome do aluno
        # 1 corresponde as notas dentro das posições d lista
print('<<<<< VOLTE SEMPRE >>>>>')
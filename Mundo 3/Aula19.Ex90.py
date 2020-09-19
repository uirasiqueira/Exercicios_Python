'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''


'''dados= {} #ou dados = dict()
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input('Média é: '))
print(f'Nome é igual a {dados["nome"]}')
print(f'A média é igual a {dados["media"]}')
if dados['media'] >=7:
    print('Situação é igual a Aprovado')
else:
    print('Situação é igual a Reprovado')'''
#No meu codigo eu não inseri situação como uma variável dentro da lista apenas como um output de if

#Guanabara methods

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media']>=7:
    aluno['situacao']='Aprovado'
elif 5<=aluno['media']<7:
    aluno['situacao']='Recuperação'
else:
    aluno['Situacao']='Reprovado'

print('-='*30)
for k, v in aluno.items():
    print(f'  - {k} é igual  {v}')
'''Crie um pequeno sistema modularizado que permita cadastrar pessoas
pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastear uma nova pessoa e
listar todas as pessoas cadastradas.'''

from Aula23 import Ex15p1

dic = {'nome': 'uira', 'idade':23}

print('-'* 40)
print(f'{"MENU PRINCIPAL":^40}')
print('-'* 40)
print('\033[1;31m1\033[m - \033[1;33mVer pessoas cadastradas\033[m')
print('\033[1;31m2\033[m - \033[1;33mCadastrar nova Pessoa\033[m')
print('\033[1;31m3\033[m - \033[1;33mSair do Sistema\033[m')
print('-'* 40)
opção = int(input('\033[1;33mSua opção: \033[m'))

if opção == 1:
    Ex15p1.lista(dic)

if opção == 2:
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    Ex15p1.cadastro(nome, idade)
    print(l)

if opção == 3:
    print('Finalizando o sistema...')


print('Fim')
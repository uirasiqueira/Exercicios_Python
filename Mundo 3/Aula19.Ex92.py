'''Crie um programa que leia, nome, ano de nascimento e carteira de trabalho e cadastreo-os
(com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário recberá
também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos
anos a pessoa vai se aposentar.'''

from datetime import date
dados={}
dados['Nome']=str(input('Nome: '))
idade= int(input('Ano de nascimento: '))
dados['DOB']= date.today().year-idade
dados['CT']= int(input('Carteira de trabalho (0 não tem): '))
if dados['CT']!= 0:
    dados['contrato']= int(input('Ano de contratação: '))
    dados['salario']= float(input('Qual o seu salário: R$ '))
    #dados['aposentadoria'] = date.today().year-dados['contrato']
    dados['aposentadoria'] = dados ['DOB'] + ((dados['contrato'] + 35) - date.today().year)
print('-='*30)
print(dados)
for k, v in dados.items():
    print(f'  -{k} tem o valor {v}')
if dados['aposentadoria'] <=35:
    print(f'Falta {35-dados["aposentadoria"]} anos para sua aposentadoria')
else:
    print('Já pode se aposentar')

#Guanabara methods
#Igual ao meu


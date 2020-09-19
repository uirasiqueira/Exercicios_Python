'''Cire um program que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas;
B) A média de idade do grupo;
C) Uma lista com todas as mulheres;
D) Um lista com todas as pessoas com idades acima da média.'''

galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0] #o 0 para pegar só a primeira letra
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma+=pessoa['idade']
    galera.append(pessoa.copy()) #Nessa situação utiliza o >> .copy <<
    while True:
        resp = str(input('Quer continuar [S/N]?: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('=-'*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')#Tamanho da lista
media = soma/len(galera)
print(f'B) A media de idade é de {media:5.2f} anos.')#5 casa ao todo e duas decimais
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo']== 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade']>= media:
        print('      ', end='')
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
print('<< ENCERRADO >>')

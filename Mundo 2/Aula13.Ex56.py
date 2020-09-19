'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final
do programa, mostre:

- A média de idade do grupo;
- Qual é o nome do homem mais velho;
- Quantas mulheres têm menos de 20 anos'''

sidade = 0
midade= 0
homemidade = 0
nomehomem = ''
mulher= 0
for c in range (1,5):
    print(f'-'*10, f'{c}° PESSOA', f'-'*10) #ou print(f'-----{c}° Pessoa -----)
    nome = str(input(f'NOME: ')).upper().strip()
    idade = int(input(f'IDADE:'))
    sexo = str(input(f'SEXO [M/F]:')).upper().strip()
    sidade = sidade + idade
    if c ==1 and sexo== 'M':
        homemidade = idade
        nomehomem = nome
    elif sexo == 'M' and idade> homemidade:
        homemidade = idade
        nomehomem = nome
    elif sexo == 'F'and idade<20:
        mulher+=1
    midade= sidade/4
print(f' A media de idade do grupo sera de {midade}')
print(f'O homem mais velho tem {homemidade} anos e se chama {nomehomem}')
print(f'Ao todo são {mulher} mulheres com menos de 20 anos')


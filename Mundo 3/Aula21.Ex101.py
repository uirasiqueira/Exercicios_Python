'''Crie um programa que tenha uma função chamada voto() que vai receber
como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições'''

from datetime import date
def voto(ano):
    idade = date.today().year - ano
    if idade < 16:
        return f'Sua idade é {idade}. Com menos de 16 anos o voto não é permitido'
    if 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos o voto é opicional'
    if 65 > idade >= 18:
        return f'Com {idade} anos o voto é obrigatório'


print(voto(ano = int(input('Qual o seu ano de nascimento? '))))

#Se eu coloco o IF após o print a variável idade não será relacionada, pois está
#no scopo local
''''Faça um programa que leia o sexo de uma pessoa, mas so aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitalização novamente ate ter um valor correto.'''


#nome = str(input('Qual o nome da pessoa? ')).strip()
#s = str(input('Qual o sexo da pessoa? ')).strip()
#while s not in 'MmFf':
#    s = str(input('Escolha entre as opções possiveis [M/F]? ')).strip()
#print(f'O sexo da pessoa e {s}')



nome = str(input('Qual o seu sexo? opção disponível [M/F]:')).upper()
while nome != 'M' and nome!= 'F':
    nome = str(input('Qual o seu sexo?[M / F]')).upper()
print('Fim')





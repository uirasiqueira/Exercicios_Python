'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra santo'''

cidade= input('Digite o nome da sua cidade:').upper()
cidade1 = cidade.split()
print('Santo' in cidade1[0])

#ou

print(cidade1[0] == 'Santo')

#ou

print(cidade[:4].upper() == "SANTO")
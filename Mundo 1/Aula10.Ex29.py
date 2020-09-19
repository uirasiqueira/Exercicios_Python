''' Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada Km acima do limite'''

v = float(input('Qual a velocidade atual do seu carro? '))
if v > 80:
    n = (v - 80)*7
    print(f'MULTADO!!!! A velocidade maxima permitida e de 80Km. \nA sua multa sera no valor de {n:.2f} euros!')
print('Tenha um bom dia e dirija com segurança.\n =====LEMBRE-SE, se beber não dirija!!=====')
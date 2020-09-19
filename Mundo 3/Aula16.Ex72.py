'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

'''numero = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze',
          'doze','treze','quatroze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
check = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
digite= int(input('Digite um número entre 0 e 20: '))
while True:
    if digite not in check:
        digite = int(input(f'Você digitou o número {digite}. Escolha novamente o número: '))
    else:
        break
print(f'Você digitou {numero[digite]} ')'''

#ou

extensos = ('zero', 'um', 'dois', 'três','quatro', 'cinco', 'seis', 'sete', 'oito','nove','dez', 'onze', 'doze', 'treze', 'quatorze','quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero = int(input('Digite um numero de 0 a 20: '))
while numero not in range(0,21):
	numero = int(input('Tente novamente.Digite um numero de 0 a 20: '))
print(f'Você digitou o numero {extensos[numero]}!')

#ou guanabrara code

''' numero = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze',
          'doze','treze','quatroze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    digite = int(input('Digite um número entre 0 e 20: '))
    if 0<=digite<=20:
        print(f'Você digitou {numero[digite]}')
        continuar = str(input('Quer continuar [S/N]:')).upper()
        if continuar == 'S':
            digite = int(input('Digite um número entre 0 e 20: '))
        else:
            break
    else:
        print('Tente novamente')
print('Obrigado')'''

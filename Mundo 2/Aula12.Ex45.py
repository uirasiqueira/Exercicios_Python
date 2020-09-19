''' Crie um programa que faça o computador jogar   Jokenpô com você'''

from random import choice
print('*.'*50)
print('                                 JOKENPÔ: Pedra, Papel, Tesoura.')
print('*.'*50)
opcao = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(opcao)
jog = input('Gostaria de jogar JOKENPO?').upper()

from time import sleep
if jog == 'sim':
   jogador = str(input('Escolha sua opção:')).upper()
   print('JO')
   sleep(0.5)
   print('KEN')
   sleep(0.5)
   print('PO!!!')
   if computador == 'PEDRA' and jogador == 'TESOURA' or computador == 'PAPEL' and jogador == 'PEDRA' or computador == 'TESOURA' and jogador == 'PAPEL':
      print('*.'*10)
      print(f'''  {jogador} vs {computador}\n    Eu ganhei!!!''')
      print('*.'*10)
   elif computador == 'PEDRA' and jogador =='PEDRA' or computador == 'PAPEL' and jogador == 'PAPEL' or computador == 'TESOURA' and jogador == 'TESOURA':
      print('*.' * 10)
      print(f'''  {jogador} vs {computador}\n    Empate!!''')
      print('*.' * 10)
   elif jogador == 'PEDRA' and computador =='TESOURA' or jogador == 'PAPEL' and computador == 'PEDRA' or jogador == 'TESOURA' and computador == 'PAPEL':
      print('*.' * 10)
      print(f'''  {jogador} vs {computador}\n    Você ganhou!!''')
      print('*.' * 10)
   else:
      print('Jogada invalida')
elif jog == 'nao':
   print('.<.>.<.>. Ok, ate a proxima .<.>.<.>.')

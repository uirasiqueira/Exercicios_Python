'''Faça um programa que mostre que mostre a tabuada de vários de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''

print('~'*20)
print('----------> Tabuada da infinito <----------')
print('~'*20)


continuar = 0
while True:
  numero = int(input('Quer ver a tabuada de qual valor?'))
  print('-' * 35)
  if numero < 0:
    break
  for c in range (0,11):
    print(f'{numero} x {c} = {numero*c}')
  print('-'*35)
print('Programa da tabuada encerrada.')
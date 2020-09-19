'''Escreve um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.

Para salários inferiores ou iguais, o aumento é de 15%.'''

s = float(int(input('Qual o salario do funcionario da Bayer:')))
if s<=1250:
    s1= 15/100*s
    s2 = s1+s
    print(f'O funcionario ira receber um aumento de R$ {s1}, totalizando um valor de R${s2}')
else:
    s3= 10/100*s
    s4=s3+s
    print(f'O funcionario ira receber um aumento de {s3}, totalizando um valor de {s4}')
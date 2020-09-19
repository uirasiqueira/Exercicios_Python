''' Faça um rograma que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar;
- Se é a hora de se alistar
- Se ele já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo'''

from datetime import date
nasc = int(input('Qual o seu ano de nascimento?'))

idade = date.today().year - nasc
falta = 18 - idade
passou = idade - 18
if idade < 18:
    print(f'Não chegou a hora do seu alistamento, mas lembre-se ao completar 18 anos compareça a junta militar mais proxima, falta apenas {falta} anos')
elif idade == 18:
    print('A sua hora chegou, compareça a junta militar mais proxima e realize o seu \033[1;33malistamento!!')
elif 30 >= idade > 18:
    print(f'O tempo de alistamento passou compareça, com \033[33mURGÊNCIA\033[m, a Junta militar mais proxima. Ja se passaram {passou} anos')
else:
    print(f'''\033[31mENLOUQUECEU\033[m?, quer ser \033[31mPRESO\033[m?\nVocê tem \033[32m{idade}\033[m anos, porra.
Ja se passaram {passou} anos.
COMPAREÇA COM URGENTE A UMA \033[32mJUNTA MILITAR!!!''')
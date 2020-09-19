'''Crie um programa onde o usuário digite uma expressão qualquer que use parêntese.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
e fechados na ordem correta.'''

'''lista = []
expressao = str(input('Digite uma expressão: '))
if expressao.count('(') - expressao.count(')')== 0:
    print('A expressão está correta')
else:
    print('A expressão está errada')'''

#ou Guanabara method

expr = str(input('Digite uma expressão: '))
pilha =[]
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada')
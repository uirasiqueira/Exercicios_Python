'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:

- Quantidade de notas;
- A maiornota;
- A menor nota;
- A média da turma;
- A situação (opcional)

 Adicione tambémas docstrings da função.'''

def notas(*n, sit=False):
    '''
    --> Função para analisar notsa e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] > 7:
            r['situação']='Boa'
        elif r['média'] >=5:
            r['situação']= 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp= notas(9, 1, 2.5, 1.5, True)
print(resp)
help(notas)
import random

ponto = {'papel':1,'tesoura':2, 'pedra':3}

while True:
    resul = random.choice(['pedra','papel','tesoura'])

    escolha = input('digite pedra,papel ou tesoura: ')

    if escolha == resul:print('empate')

    elif ponto:
        pass

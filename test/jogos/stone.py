import random

ponto = {'papel':1,'tesoura':2, 'pedra':3}

while True:
    resul = random.choice(['pedra','papel','tesoura'])

    escolha = input('digite pedra,papel ou tesoura: ')

    if escolha == resul:print('empate')

    elif escolha == "papel":
        if resul == 'pedra': print('ganhou')
        
        else: print('perdeu')
    elif escolha == 'pedra':
        if resul == 'tesoura': print('ganhou')

        else: print('perdeu')
    elif escolha == 'tesoura':
        if resul == 'papel': print('ganhou')

        else: print('perdeu')
    else: print('invalido digite --papel, pedra ou tesoura--')
    print(resul)

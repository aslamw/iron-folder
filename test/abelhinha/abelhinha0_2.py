import numpy as np
import os,time,random
coluna = 4
linha = 1
n = 0

while n <= 100:
    campo = np.array([[0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0]])
    a = ''
    time.sleep(0.5)
    os.system('cls')
    try:
        campo[coluna][linha]= 1
    except:
        print(f'olha a merda {coluna},{linha} Game Over')
        break

    for i in range(len(campo)):
        a+='\n'
        for e in range(len(campo[i])):
            if campo[i][e] == 0:
                a+=' '
            else:
                a+=' 0'
    print([coluna,linha])
    print(a)
    n += 1

    key = ['sima','esquerda','baixo','direita']
    lugar = random.choice(key)
    if lugar == 'sima':
        coluna -= 1
    elif lugar == 'esquerda':
        linha -= 1
    elif lugar == 'baixo':
        coluna += 1
    elif lugar == 'direita':
        linha += 1
    print(lugar)

    '''
    if linha == 8:#baixo
        coluna += 1
        tempo = 1
    elif coluna == 0:#direita
        linha += 1
    elif tempo == 0:#sima
        coluna -= 1
    elif coluna == 4:#esquerda
        linha -=1
    elif linha == 1:
        tempo = 0'''
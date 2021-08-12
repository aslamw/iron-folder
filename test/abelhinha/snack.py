import numpy as np
import os,time,random
import keyboard as kb

coluna = 4
linha = 0
n = 1

def loop(x):
    global coluna,linha
    if x == 1:
        if coluna - 1 >= 0 :
            coluna -= 1
        else:
            print('Game Over')
    elif x == 2:
        if linha - 1 >= 0:
            linha -= 1
        else:
            print('Game Over')
    elif x == 3:
        if coluna + 1 >= 0:
            coluna += 1
        else:
            print('Game Over')
    elif x == 4:
        if linha + 1 >= 0:
            linha += 1
        else:
            print('Game Over')
campo = np.array([[0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0]])

while True:
    campo = np.array([[0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0]])
    a = ''


    try:
        if kb.is_pressed('w') :#sima
            n = 1
        elif kb.is_pressed('a'):#esquerda
            n = 2
        elif kb.is_pressed('s'):#baixo
            n = 3
        elif kb.is_pressed('d'):#direita
            n = 4

        loop(n)
        time.sleep(0.5)
        os.system('cls')

        campo[coluna][linha]= 1
    except:
        print(f'olha a merda {coluna},{linha} Game Over')
        break

    print([coluna,linha])
    print(a)
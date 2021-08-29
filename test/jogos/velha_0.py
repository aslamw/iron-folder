import numpy as np
import random

p = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
resul = [1,2,3],[1,4,7],[3,6,9],[7,8,9],[2,5,8],[1,5,9],[3,5,7]
x = []
o = []
valor = []

print(f'  1| 2 | 3 \n------------\n 4 | 5 | 6 \n------------\n 7 | 8 | 9 ')

while True:
    posicao = int(input('digite a posição: '))

    if posicao in valor: print('já foi escolhido')

    else:
        p[posicao] = 'x'
        x.append(posicao)
        valor.append(posicao)

    while True:
        posicao2 = random.randint(1,9)
        if posicao2 not in valor:
            valor.append(posicao2)
            p[posicao2] = 'o'
            o.append(posicao2)
            break 

    print(f' {p[1]} | {p[2]} | {p[3]} \n------------\n {p[4]} | {p[5]} | {p[6]} \n------------\n {p[7]} | {p[8]} | {p[9]} ')

    print(valor)
    if sum(x) in resul:
        print('ganhou')
        break

    elif sum(o) in resul:
        print('perdeu')
        break

import numpy as np
p = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
x = ['x','o']

print(f'  1| 2 | 3 \n------------\n 4 | 5 | 6 \n------------\n 7 | 8 | 9 ')

while True:
    posicao = int(input('digite a posição'))
    p[posicao] = 'x'

    print(f' {p[1]} | {p[2]} | {p[3]} \n------------\n {p[4]} | {p[5]} | {p[6]} \n------------\n {p[7]} | {p[8]} | {p[9]} ')

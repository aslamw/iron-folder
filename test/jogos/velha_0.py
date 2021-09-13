import random,os

p = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
resul = [[1,2,3],[1,4,7],[3,6,9],[7,8,9],[2,5,8],[1,5,9],[3,5,7]]
x = []
o = []
valor = []

print(f'  1| 2 | 3 \n------------\n 4 | 5 | 6 \n------------\n 7 | 8 | 9 ')

def tratamento(x):
    global resul
    for i in range(len(resul)):
            parte = 0
            for ii in range(len(resul[i])):
                if resul[i][ii] in x: parte += 1
            if parte == 3: return True


while True:
    posicao = int(input('digite a posição: '))

    if posicao in valor: print('já foi escolhido')

    else: #coloca o x
        p[posicao] = 'x'
        x.append(posicao)
        valor.append(posicao)
    if len(valor) == 9:# ver se já empatou
        print('empate')
        break

    if len(x) >= 3:
        if tratamento(x):
            os.system('clear')
            print('ganhou')
            break

    while True:# sistema de escolha
        posicao2 = random.randint(1,9)
        if posicao2 not in valor:
            valor.append(posicao2)
            p[posicao2] = 'o'
            o.append(posicao2)
            break 
    
    if tratamento(o):
        os.system('clear')
        print('perdeu')
        break

    os.system('clear')
    print(f' {p[1]} | {p[2]} | {p[3]} \n------------\n {p[4]} | {p[5]} | {p[6]} \n------------\n {p[7]} | {p[8]} | {p[9]} ')

    print(valor)

    '''for i in resul:#Ver ganhador
        if str(resul[i]) in str(x):
            print('ganhou')
        elif o in resul:
            print('perdeu')'''
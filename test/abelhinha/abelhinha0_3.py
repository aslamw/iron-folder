import numpy as np
import os,time,random

#campo
matrix = np.array([[0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0]])
campo = ''

mover = {'coluna':[], 'lista':[]}#base de movimento

class abelhinha:
    def __init__(self,n_abelhas):
        self.limit = 9,0#parede
        self.n_abelhas = n_abelhas
        self.posicao = {'sima':-1,'baixo':1,'direita':1,'esquerda':-1}
    def procura(self):
        global mover

        if mover['coluna']:
#          posiçãode cada
           for i in range(self.n_abelhas):
                local = random.choice('sima','baixo','direita','esquerda')
                #coluna
                if local == 'sima' or 'baixo':
                    if mover['coluna'] + self.posicao[local] <= 9:
                        if mover['coluna'] + self.posicao[local]  >= 0:
                            mover['coluna'][i] += self.posicao[local]
                #linha
                elif local == 'direita' or 'esquerda':
                    if mover['linha'] - self.posicao[local] <= 9:
                        if mover['linha'] - self.posicao[local]  >= 0:
                            mover['coluna'][i] -= self.posicao[local]




    '''for i in range(len(matrix)):#montar imagem
        a+='\n'
        for e in range(len(matrix[i])):
            if matrix[i][e] == 0:
                a+=' '
            else:
                a+=' 0'

    ia = abelhinha(5,0.5)#vida a abelha
    dados = ia.movimento()

    for  i in range(len(dados['coluna'])):#ela andando
        matrix[dados['coluna'][i]][dados['linha'][i]]=1

    print(matrix,'\n')
    n+=1'''

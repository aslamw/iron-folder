import matplotlib.pyplot as ptl
import numpy as np
import pandas as pd

class analize():
    def __init__(self,pais):
        self.pais = pais
        self.tabelaPip = pd.read_csv('matplotlib\dados\conta.csv')
        self.key = self.tabelaPip.keys()
        self.paises = self.tabelaPip['Country Name']
    def tratamento(self):
        for i in range(len(self.paises)): 
            if self.paises[i] == self.pais: return i
    def grafico(self,posicao):
        Brasilpip = []
        for i in range(4,len(self.key)): Brasilpip.append(self.tabelaPip[self.key[i]].loc[posicao])
        dados = np.array(Brasilpip)

        ptl.plot(dados,'b')
        ptl.grid()
        ptl.show()

while True:
    nome = input('digite o nome do país em inglês: ')

    resul = analize(nome)
    resul.grafico(resul.tratamento())

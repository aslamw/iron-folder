import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

class jan():
    def __init__(self):
        self.dados = pd.read_csv('test/dados/conta.csv')
        self.key = self.dados.keys()#pega as colunas
        self.paises = self.dados[self.key[0]]#pega os nomes dos países
        self.Total_dados = {}
        self.keys_tratado = self.key[4:-1]#keys tratadas
        
    def mostrar(self):
        while True:
            pa = input('Digite :').split(',')#nome tem que ser em Inglês
            print(pa)
            for i in pa:
                print(i)
                resul = np.array(self.Total_dados[i])
                plt.plot((resul),label=i)
                plt.title('PIB dos países')
            plt.legend()
            plt.show()

    def tratar(self):
        for o in range(len(self.paises)):#caminho dos países
            PIB = []
            for i in range(4,len(self.key)-1):#caminho dos anos
                PIB.append(self.dados[self.key[i]].loc[o])#pega os valores do PIB dos países
            self.Total_dados[self.paises[o]]=PIB
            
tratado = jan()
tratado.tratar()
tratado.mostrar()
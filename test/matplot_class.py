import matplotlib.pyplot as mtl
import numpy as np

class grafico():
    def __init__(self,basex,basey):
        self.basex = basex
        self.basey = basey

    def tabela(self):
        mtl.plot(self.basex,self.basey,'--b')
        mtl.show()

basex = np.array([1,2,3,4])
basey = np.array([2,3,4,5])

inicio= grafico(basex,basey)
inicio.tabela()

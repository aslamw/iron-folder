import scipy as sp
import numpy as np
import math as mt
from scipy.sparse import csr_matrix
from scipy.optimize import root,minimize
#NumPy é capaz de encontrar raízes para polinômios e equações lineares, mas não pode encontrar raízes para equações não lineares

def eqn(x):
    return x + mt.cos(x)

myroot = root(eqn, 0)#fun - uma função que representa uma equação.  x0 - uma estimativa inicial para a raiz.
print(myroot.x)
print('todas as informações',myroot)

#encontrando mínimos
'''fun - uma função que representa uma equação.
    x0 - uma estimativa inicial para a raiz.
    método - nome do método a ser usado. Valores legais:
        'CG'
        'BFGS'
        'Newton-CG'
        'L-BFGS-B'
        'TNC'
        'COBYLA'
        'SLSQP'
    callback - função chamada após cada iteração de otimização.
    options - um dicionário que define parâmetros extras:'''
def eqn(x):
    return x**2 + x + 2

mymin = minimize(eqn,0,method='BFGS')
print(50*'-')
print(mymin)

#dados esparsos
'''Dados esparsos são dados que contêm principalmente elementos não utilizados 
(elementos que não carregam nenhuma informação).Pode ser uma matriz como esta:
[1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0]
Dados esparsos: é um conjunto de dados em que a maioria dos valores dos itens é zero.
Matriz Densa: é o oposto de uma matriz esparsa: a maioria dos valores não é zero.
Na computação científica, quando lidamos com derivadas parciais em álgebra linear, 
encontraremos dados esparsos.
produtos vetoriais de matriz mais rápidos
CSC - coluna esparsa compactada. Para aritmética eficiente, 
corte rápido de colunas.
CSR - Linha esparsa compactada. Para corte rápido de fileiras, 
'''
arr = np.array([0,0,0,0,0,1,1,0,2])
arr1 = np.array([0,0,0],[0,0,1],[1,0,2])
print(csr_matrix(arr))
print(csr_matrix(arr1).data)#visualizando os dados ca a 'data' apropriada menos os 0
print(csr_matrix(arr1).count_nonzero())#conta os valores diferentes de 0

mat = csr_matrix(arr1)
mat.eliminate_zeros()#remove a entrada de 0 na matrix
print(mat)
arr1 = np.array([0,0,0],[0,0,1],[1,0,2])
mat = csr_matrix(arr1)
mat.sum_duplicates()#Elimina entradas duplicadas
print(mat)
arr1 = np.array([0,0,0],[0,0,1],[1,0,2])
converter = csr_matrix(arr1).tocsc()#converte csr em csc
print(converter)


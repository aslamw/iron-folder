import numpy as np
import os,time

campo = np.array([[0,0,0,0,0,0,0,0,0,0],
                  [0,0,1,1,1,0,0,0,0,0],
                  [0,0,1,0,0,0,0,0,0,0],
                  [0,0,1,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0]])
a = ''

for i in range(len(campo)):
    a+='\n'
    for e in range(len(campo[i])):
        if campo[i][e] == 0:
            a+=' '
        else:
            a+=' 0'
print(a)

campo[0][1]=2
print(campo)
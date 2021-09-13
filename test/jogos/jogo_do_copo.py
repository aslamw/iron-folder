import numpy as np
import random, os, time

img = np.array([[0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0]])
            
'''img = np.array([[1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1]])'''

print(img)
for i in range(100):
    os.system('cls')
    ver = [random.randint(0,4),random.randint(1,9)]
    nv = img.copy()
    nv[ver[0]][ver[1]]=1
    print(ver)
    print(nv)
    time.sleep(0.5)

import matplotlib.pyplot as plt
import numpy as np

dados = np.array([1,2,3,4,5,6,7])
plt.plot(dados , 'r--')
fig = plt.gcf()#salva em uma variavel a imagem
print(fig)

fig.savefig('matplotlib/teste.png',format='jpg')

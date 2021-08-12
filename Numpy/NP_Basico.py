import numpy as np

#base 1 de estudos
base = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(base)
print(base.ndim)#mostra as dimenções
print(base.shape)#mosta linhas e colunas
print(base.reshape(-1))#diminue para 1 dimenção
for x in np.nditer(base, flags=['buffered'], op_dtypes=['S']):#modifica enquanto percorre
  print(x)
for x in np.nditer(base[:, ::2]):#pula de 1 em 1 de cada linha
  print(x)
for idx, x in np.ndenumerate(base):#mostra o numero de repetições
  print(idx, x)

a = base[0],base[2]
b = base[1],base[3]
print(np.concatenate((a,b),axis=1))#junta duas bases e axis pra ser 2 dimenção



#base 2 de estudo
base2 = np.array([1,2,3,4],ndmin=5)#coloca 5 dimenções [start:end:step]
print(base2)
base2 = np.array([1,2,3,4],dtype='S')
print(base2)
print(base2.astype('i'))#faz um copia com outro tipo
print(base2.base)#pra saber se é original ou copia
print(base2.reshape(2,2))#reorganeza as dimenções

'''
i - inteiro
b - boleano
u - inteiro sem sinal
f - flutuar
c - flutuação complexa
m - timedelta
M - data hora
O - objeto
S - fragmento
U - string Unicode
V - pedaço fixo de memória para outro tipo (vazio)

Por i, u, f, Se Upodemos definir o tamanho também.
dtype='i4'
'''

#base 3 de estudos
#base3 = base.copy()#se usar .view() oque alterar em um muda também no outro
base3 = np.array([[2,4,8],[5,7,8]])
base33 = np.array([[1,2,3],[7,9,2]])
print(np.concatenate((base3,base33),axis=1))#junta dois arrays e coloca ele em 2D
print(np.stack((base3,base33),axis=1))#metodo de junção por eixo
print(np.hstack((base3,base33)))#emplilha ao longo das linhas
print(np.vstack((base3,base33)))#emplilha ao longo das colunas
print(np.dstack((base3,base33)))#emplilha ao longo da altura, que é o mesmo que profundidade
base3 = np.array([1,2,3,4,5,6,7,8,9,10])

print(np.array_split(base3,3))#divide a matriz
print(np.hsplit(base33,3))#divide matriz de n-dimenções
print(np.where(base33 == 2))#localiza no index e a matrix // base%2 olha só pares e 1 ímpas
print(np.searchsorted(base3,2))#realiza uma pesquisa binária na matriz e retorna o índice onde o valor especificado seria inserido para manter a ordem de pesquisa.  side='right' para ler mais a direita
print(np.sort(base33))#ordena os números

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]#filtragem de array os False são excluidos

print(newarr)
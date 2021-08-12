import matplotlib.pyplot as plt
import numpy as np

#Dados da tabela 1
pontox = np.array([6,5,8,12,1,2,56,7,9,134])
pontoy = np.array([3,5,78,9,12,65,2,34,19,45])

pontox1 = np.array([1,4,7,10,56,69,70,83,81,100])
pontoy1 = np.array([2,5,8,11,59,72,75,85,83,110])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':10}

#tabela 1
plt.subplot(2,4,1)
plt.plot(pontox1,pontoy1,'*-.r',ms=5,lw=2)
plt.plot(pontox,pontoy,'o--y',ms=10,mec='k',mfc='b',lw=4)

plt.title('tabela louca',fontdict = font1)
plt.ylabel('louco de y',fontdict = font2)
plt.grid(c='g',ls='--',lw=1)

#dados da tabela 2
pontox = np.array([1,2,4,7,8])
pontoy = np.array([2,3,5,8,7])

pontox1 = np.array([1,2,4,7,8])
pontoy1 = np.array([2,5,10,8,7])
#tabela 2
plt.subplot(2,4,2)
plt.plot(pontox,pontoy,'--b')
plt.plot(pontox1,pontoy1,'--b')

plt.title('tabela louca',fontdict = font1)
plt.xlabel('louco de x',fontdict = font2)
plt.ylabel('louco de y',fontdict = font2)
plt.grid(c='r',ls='--',lw=1,axis='x')

#tabela 3

plt.subplot(2,4,3)
plt.plot(pontox,pontoy,'y')
plt.plot(pontox1,pontoy1,'y')

plt.title('tabela louca',fontdict = font1)
plt.xlabel('louco de x',fontdict = font2)
plt.ylabel('louco de y',fontdict = font2)
plt.grid(c='b',lw=1,axis='y')

#tabela 4

plt.subplot(2,4,4)
plt.scatter(pontox,pontoy,cmap='viridis')
plt.scatter(pontox1,pontoy1,cmap='viridis')

plt.title('tabela louca',fontdict = font1)
plt.xlabel('louco de x',fontdict = font2)
plt.ylabel('louco de y',fontdict = font2)
plt.grid(c='b',lw=1,axis='y')
plt.colorbar()

#tabela 5

plt.subplot(2,4,5)
plt.scatter(pontox,pontoy,alpha=0.5)
plt.scatter(pontox1,pontoy1,alpha=0.5)

plt.title('tabela louca',fontdict = font1)
plt.xlabel('louco de x',fontdict = font2)
plt.ylabel('louco de y',fontdict = font2)

#tabela 6
plt.subplot(2,4,6)
plt.bar(pontox,pontoy,width=0.2)
plt.bar(pontox1,pontoy)

plt.title('tabela louca',fontdict = font1)
plt.xlabel('louco de x',fontdict = font2)
plt.ylabel('louco de y',fontdict = font2)
plt.grid(c='b',lw=1,axis='y')

#tabela 7
plt.subplot(2,4,7)
plt.barh(pontox,pontoy,height=0.2)
plt.barh(pontox1,pontoy)

plt.title('tabela louca',fontdict = font1)
plt.xlabel('louco de x',fontdict = font2)
plt.ylabel('louco de y',fontdict = font2)
plt.grid(c='b',lw=1,axis='x')

#tabela 8
plt.subplot(2,4,8)
plt.hist(pontox)


plt.title('tabela louca',fontdict = font1)
plt.xlabel('louco de x',fontdict = font2)
plt.ylabel('louco de y',fontdict = font2)
plt.grid(c='b',lw=1,axis='x')

#tabela 9
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.subplot(2,5,9)
plt.pie(y, labels = mylabels)
plt.legend()

#tabela 10
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.subplot(2,5,10)
plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)

plt.suptitle('bota tabela louca nisso',fontdict = font1)
plt.show()

import numpy as np
from numpy import append, random
import matplotlib.pyplot as plt
from scipy.stats.stats import chisquare
import seaborn as sb

print(random.rand())#retorna uma flutuação aleatória entre 0 e 1.
print(random.rand(3,5))#com 3 linhas e 5 numeros aleatoriaos.

print(random.randint(100))#um numero aleatorio inteiro de 1 á 100
print(random.randint(100,size=(3,5)))#Gere uma matriz 2-D com 3 linhas, cada linha contendo 5 inteiros aleatórios de 0 a 100
print(random.choice([3,5,7,9],size=(3,5)))#Gere uma matriz 2-D que consiste nos valores do parâmetro da matriz (3, 5, 7 e 9):

'''Gere uma matriz 1-D contendo 100 valores, onde cada valor deve ser 3, 5, 7 ou 9.
A probabilidade do valor ser 3 está definida como 0,1
A probabilidade do valor ser 5 é de 0,3
A probabilidade do valor ser 7 está definida como 0,6
A probabilidade do valor ser 9 é definida como 0
a soma de todas as probalidades tem que ser igual a 1'''

print(random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100)))
arr = np.array([1, 2, 3, 4, 5])

print(random.shuffle(arr))#Embaralhe aleatoriamente os elementos da seguinte matriz
print(random.permutation(arr))#Gere uma permutação aleatória de elementos da seguinte matriz

#Distplot significa gráfico de distribuição, toma como entrada uma matriz e plota uma curva correspondente à distribuição de pontos na matriz
sb.histplot([0,1,2,3,4,5])#Traçando um Displot.
plt.show()
sb.distplot([0,1,2,3,4,5,6,7],hist=False)#Distplot sem o Histograma
plt.show()
#---------------distribuição normal(gaussiana)
x = random.normal(loc=1, scale=2, size=(2, 3))#Ele se ajusta à distribuição de probabilidade de muitos eventos, (Média) onde existe o pico do sino.,
#(Desvio padrão) quão plana deve ser a distribuição do gráfico.,size - A forma da matriz retornada.
sb.histplot(x)
plt.show()

#-------------------distribuição Binomial
sb.distplot(random.normal(loc=50, scale=5, size=1000),hist=False,label='normal')
sb.distplot(random.binomial(n=10, p=0.5, size=1000),hist=False,label='binominal')#A distribuição binomial é uma distribuição discreta .
#n - número de tentativas., p - probabilidade de ocorrência de cada tentativa (por exemplo, para lançamento de moeda 0,5 cada)
#size - A forma da matriz retornada.
plt.legend()#permite usar labels
plt.show()

#----------------------------Distribuição Veneno
num = random.poisson(lam=2, size=10)#Gere uma distribuição 1x10 aleatória para a ocorrência 2
#lam - taxa ou número conhecido de ocorrências, por exemplo, 2 para o problema acima.
sb.distplot(num,kde=False)
plt.show()

#------------------------------Distribuição Uniforme
num = random.uniform(size=(2,3))
sb.distplot(num)#Usado para descrever a probabilidade onde cada evento tem chances iguais de ocorrer.
#a - limite inferior - padrão 0 .0.   b - limite superior - padrão 1.0.
plt.show()

#------------------------------Distribuição Logística
sb.distplot(random.logistic(loc=1,scale=2,size=(2,3)))#A distribuição logística é usada para descrever o crescimento.
#Usado extensivamente em aprendizado de máquina em regressão logística, redes neurais etc.
plt.show()
#loc- quer dizer, onde está o pico. Padrão 0.  scale- desvio padrão, a planura de distribuição. Padrão 1.  size - A forma da matriz retornada.

#-----------------------------Distribuição Multinomial
'''A distribuição multinomial é uma generalização da distribuição binomial.
Ele descreve os resultados de cenários multinomiais, ao contrário do binômio, onde os cenários devem ser apenas um de dois. por exemplo, tipo de sangue de uma população, resultado do lançamento de dados
Possui três parâmetros:
n - número de resultados possíveis (por exemplo, 6 para lançamento de dados).
pvals - lista de probabilidades de resultados (por exemplo, [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] para lançamento de dados).
size - A forma da matriz retornada.'''
sb.distplot(random.multinomial(n=6,pvals=[1/6,1/6,1/6,1/6,1/6,1/6],))
plt.show()

#------------------------------------Distribuição exponencial
sb.distplot(random.exponential(scale=2,size=(2,3)))#scale - inverso da taxa (ver lam na distribuição de Poisson) 
#padroniza para 1.0. size - A forma da matriz retornada.
plt.show()

#------------------------------------Distribuição chi quadrado
sb.distplot(random.chisquare(df=2,size=(2,3)))#A distribuição do qui quadrado é usada como base para verificar a hipótese.
#df - (grau de liberdade).  size - A forma da matriz retornada.
plt.show()

#-------------------------------------Distribuição Rayleigh
sb.distplot(random.rayleigh(scale=2, size=(2,3)))#A distribuição de Rayleigh é usada no processamento de sinais.
#scale - (desvio padrão) decide quão plana a distribuição será o padrão 1.0).  size - A forma da matriz retornada.
plt.show()

#-------------------------------------Distribuição de pareto
sb.distplot(random.pareto(a=2, size=(2,3)))#Uma distribuição seguindo a lei de Pareto, ou seja, distribuição 80-20 (fatores de 20% causam resultado de 80%).
#a - parâmetro de forma.  size - A forma da matriz retornada.
plt.show()

#-------------------------------------Distribuição Zipf
x = random.zipf(a=2, size=(2, 3))#As distribuições Zipf são usadas para amostrar dados com base na lei de zipf.
'''Lei de Zipf: Em uma coleção, o enésimo termo comum é 1 / n vezes do termo mais comum. Por exemplo, a 5ª palavra comum em inglês ocorre quase 1/5 vezes a partir da palavra mais usada.
a - parâmetro de distribuição.   size - A forma da matriz retornada.'''
sb.distplot(x[x<10])
plt.show()
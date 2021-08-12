import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

x = [1,2,3,4]
y = [4,5,6,7]
z = np.add(x,y)#junta os dois
print(z)

#unfuc função universal
print(50*'-')
def soma(x,y):
    return x+y

som = np.frompyfunc(soma,2,1)#criando um metodo função universal
print(som([1,2,3,4],[5,6,7,8]))

#Aritmética simples
print(50*'-')
arr1 = np.array([2,3,4,5])
arr2 = np.array([4,8,7,3])

print(np.add(arr1,arr2))#soma
print(np.subtract(arr1,arr2))#subtração
print(np.multiply(arr1,arr2))#multiplicação
print(np.divide(arr1,arr2))#divisão
print(np.power(arr1,arr2))#espoente
print(np.mod(arr1,arr2))# (arr1% arr2) remainder funciona tb
print(np.divmod(arr1,arr2))# arr1 /arr2 e (arr1% arr2)
x = np.array([-1,-3,-2,1,-5])
print(np.absolute(x))#todos vão ficar positivos

#Decimais de arredondamento

print(np.trunc([-3.1666, 3.6667])) #Remova os decimais e retorne o número flutuante mais próximo de zero. Use as funções trunc()e fix().
print(np.around(3.1666, 2)) #A around()função incrementa o dígito anterior ou decimal em 1 se> = 5, caso contrário, não fará nada.
#Por exemplo, arredondar para 1 casa decimal, 3,16666 é 3,2

print(np.floor([-3.1666, 3.6667])) #A função floor () arredonda o decimal para o inteiro inferior mais próximo.
#Por exemplo, o piso de 3.166 é 3.

print(np.ceil([-3.1666, 3.6667])) #A função ceil () arredonda o decimal para o inteiro superior mais próximo.
#Por exemplo, o teto de 3,166 é 4.

#registro numpy
arr = np.arange(1, 10)

print(np.log2(arr)) #Use a log2()função para realizar o registro na base 2
print(np.log10(arr)) #Use a log10()função para realizar o registro na base 10.
print(np.log(arr)) #Use a log()função para realizar o registro na base e.

nplog = np.frompyfunc(2, 1)

print(nplog(100, 15))#NumPy não fornece nenhuma função para obter log em qualquer base, 
#então podemos usar a frompyfunc()função junto com a função embutida math.log()com dois parâmetros de entrada e um parâmetro de saída

#Somações NumPy

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

print(np.add(arr1, arr2))#Qual é a diferença entre soma e adição? A adição é feita entre dois argumentos, enquanto a soma ocorre em n elementos.
print(np.sum([arr1, arr2]))

print(np.sum([arr1, arr2], axis=1)) #Se você especificar axis=1, NumPy somará os números em cada matriz.

arr = np.array([1, 2, 3])

print(np.cumsum(arr)) #Soma cumulativa significa adicionar parcialmente os elementos na matriz.
#Por exemplo, a soma parcial de [1, 2, 3, 4] seria [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4] = [1, 3, 6, 10].
#Faça a soma parcial com a cumsum()função.

#Produtos NumPy
arr = np.array([1, 2, 3, 4])
print(np.prod(arr))#Para encontrar o produto dos elementos em uma matriz, use a prod()função.

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

print(np.prod([arr1, arr2], axis=1))#mostra o produto de cada 1 arr

#produto acumulativo
arr = np.array([5, 6, 7, 8])

print(np.cumprod(arr))#Produto cumulativo significa retirar o produto parcialmente.
#Por exemplo, o produto parcial de [1, 2, 3, 4] é [1, 1 * 2, 1 * 2 * 3, 1 * 2 * 3 * 4] = [1, 2, 6, 24]
#Faça a soma parcial com a cumprod()função.

#Diferenças NumPy
arr = np.array([10, 15, 25, 5])

print(np.diff(arr))#Uma diferença discreta significa subtrair dois elementos sucessivos.
#Por exemplo, para [1, 2, 3, 4], a diferença discreta seria [2-1, 3-2, 4-3] = [1, 1, 1]
#Para encontrar a diferença discreta, use a diff()função.

print(np.diff(arr, n=2))#Podemos realizar esta operação repetidamente, dando parâmetro n.
#Por exemplo, para [1, 2, 3, 4], a diferença discreta com n = 2 seria [2-1, 3-2, 4-3] = [1, 1, 1], 
#então, uma vez que n = 2, faremos mais uma vez, com o novo resultado: [1-1, 1-1] = [0, 0]

#NumPy LCM Menor Múltiplo Comum

num1 = 4
num2 = 6
print(np.lcm(num1, num2))#12 porque esse é o menor múltiplo comum de ambos os números (4 * 3 = 12 e 6 * 2 = 12).

arr = np.array([3, 6, 9])
print(np.lcm.reduce(arr))#O reduce()método usará o ufunc, neste caso a lcm()função, em cada elemento e reduzirá o array em uma dimensão.
#18 porque esse é o menor múltiplo comum de todos os três números (3 * 6 = 18, 6 * 3 = 18 e 9 * 2 = 18).

#NumPy GCD de maior denominador comum
num1 = 6
num2 = 9
print(np.gcd(num1, num2))#O GCD (maior denominador comum), também conhecido como HCF (maior fator comum) é o maior número que é um fator comum de ambos os números.
#3 por ser o número mais alto, os dois números podem ser divididos (6/3 = 2 e 9/3 = 3).

arr = np.array([20, 8, 32, 36, 16])
print(np.gcd.reduce(arr))#O reduce()método usará o ufunc, neste caso a gcd()função, em cada elemento e reduzirá o array em uma dimensão.
#4 porque esse é o número mais alto pelo qual todos os valores podem ser divididos.

#Funções trigonométricas:    NumPy fornece os ufuncs sin(), cos()e tan()que os valores Leve em radianos e produzir os correspondentes sin, cos e valores tan.
print(np.sin(np.pi/2))#Encontre o valor do seno de PI / 2

'''Converter graus em radianos
Por padrão, todas as funções trigonométricas usam radianos como parâmetros, mas também podemos converter radianos em graus e vice-versa em NumP.'''
arr = np.array([90, 180, 270, 360])
print(np.deg2rad(arr))#os valores em radianos são pi / 180 * degree_values.

arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])#Radianos em graus
print(np.rad2deg(arr))#Converta todos os valores da seguinte matriz em graus

#Encontrando ângulos
print(np.arcsin(1.0))#Encontre o ângulo para todos os valores de seno na matriz
'''Encontrar ângulos a partir dos valores de seno, cos, tan. Ex: sin, cos e tan inverso (arcsin, arccos, arctan).
NumPy fornece ufuncs arcsin(), arccos()e arctan()que produzem valores de radiano para sin, cos e os valores tan dado correspondente.'''

#Hipotenias
base = 3
perp = 4
print(np.hypot(base, perp))#Encontre as hipotecas para 4 bases e 3 perpendiculares
'''Encontrando hipoteninas usando o teorema de Pitágoras em NumPy.
NumPy fornece a hypot()função que obtém os valores básicos e perpendiculares e produz hipoteninas com base no teorema de Pitágoras.'''

#Funções hiperbólicas NumPy
print(np.sinh(np.pi/2))#Encontre o valor sinh de PI / 2
'''NumPy fornece os ufuncs sinh(), cosh()e tanh()que assumem valores em radianos e produzem os valores sinh, cosh e tanh correspondentes.'''

#Encontrando ângulos
print(np.arcsinh(1.0))
'''Encontrar ângulos a partir dos valores de seno hiperbólico, cos, tan. Por exemplo, sinh, cosh e tanh inverso (arcsinh, arccosh, arctanh).
Numpy fornece ufuncs arcsinh(), arccosh()e arctanh()que produzem valores em radianos para os valores sinh, cosh e tanh correspondentes fornecidos.'''

#Ângulos de cada valor em matrizes
arr = np.array([0.1, 0.2, 0.5])
print(np.arctanh(arr))#Encontre o ângulo para todos os valores tanh na matriz

#Operações de conjunto NumPy
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
print(np.unique(arr))#Converta a seguinte matriz com elementos repetidos em um conjunto
'''
O que é um conjunto. Um conjunto em matemática é uma coleção de elementos únicos.
Os conjuntos são usados ​​para operações que envolvem operações frequentes de intersecção, união e diferença.Criar conjuntos em NumPy
Podemos usar o unique() método do NumPy para encontrar elementos exclusivos de qualquer array. Por exemplo, crie um array de conjunto, 
mas lembre-se de que os arrays de conjunto devem ser apenas arrays 1-D.
'''

#Encontrando União
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
print(np.union1d(arr1, arr2))#Encontre a união das duas seguintes matrizes de conjunto
#Para encontrar os valores exclusivos de duas matrizes, use o union1d() método

#Encontrando Cruzamento
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
print(np.intersect1d(arr1, arr2, assume_unique=True))#Encontre a interseção das duas seguintes matrizes de conjunto
#Para localizar apenas os valores que estão presentes em ambas as matrizes, use o intersect1d() método.
'''
o intersect1d()método leva um argumento opcional assume_unique, 
que se definido como True pode acelerar o cálculo. Deve sempre ser definido como True ao lidar com conjuntos.
'''

#Encontrando Diferença
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
print(np.setdiff1d(set1, set2, assume_unique=True))#Encontre a diferença entre set1 e set2
#Para encontrar apenas os valores no primeiro conjunto que NÃO estão presentes no conjunto de segundos, use o setdiff1d() método.
'''
O setdiff1d() método leva um argumento opcional assume_unique, que se definido como True pode acelerar o cálculo. 
Deve sempre ser definido como True ao lidar com conjuntos.
'''

#Encontrando Diferença Simétrica
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
print(np.setxor1d(set1, set2, assume_unique=True))#Encontre a diferença simétrica do conjunto1 e conjunto2
#Para encontrar apenas os valores que NÃO estão presentes em AMBOS os conjuntos, use o setxor1d() método.
'''
O setxor1d() método leva um argumento opcional assume_unique, que se definido como True pode acelerar o cálculo.
Deve sempre ser definido como True ao lidar com conjuntos.
'''
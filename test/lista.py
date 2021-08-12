import copy as cop

a = ['oi','ui','jk']
b = a
b.append('la')
print(a)
print(b)

c = a[:]
c.append('feijão')
d = a.copy()
d.append('arroz')
print(c)
print(d)

#O mais seguro
a = [['yu','mj'],[34,67]]
e = cop.deepcopy(a)
e.append('gfsfg')
print(e)
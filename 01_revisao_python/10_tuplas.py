t=(4,)
print(t)
print(len(t))

t=(4,'abc',3.14,'123345',True)
print(t)
print(len(t))

print(t[0])
print(t[-1])
print(t[1:3])
print(t[2:])

b=(1,2)+(3,4)
print(b)

c=(1,2)*3
print(c)

s = 'ifrn'
res = tuple(c*3 for c in s)
print(res)
print(type(res))

t = ('z','b','2','c','a','x','r','x','2','5','2')
lista = list(t)
print(t)
print(lista)
print(type(lista))
#lista.sort()
print(lista)

tupla = tuple(lista)
print(tupla)
print(type(tupla))

#print(tupla.index('x'))
print(tupla.index('2',9))
print(tupla.count('2'))

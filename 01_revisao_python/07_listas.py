L=[4,'abc',1.23]
M=['fgh',5.6,10,145]
print(len(L))
X=L+M
print(X)
print(len(X))
print(3*L)

#verificar associacao de lista
print('abc' in L)

#iterar a lista
for x in L:
    print(x)

#list comprehensxions
res = [c*4 for c in 'abc']
print(res)
print(type(res))

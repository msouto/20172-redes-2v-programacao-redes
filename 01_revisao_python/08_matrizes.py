#matrizes
m = [[1,2,3],[4,5,6],[7,8,9]]
print(m)
#imprimir a segunda linha
print(m[1])

#imprimir o elemento 8
print(m[2][1])

#imprimir os elemntos 2,5,8
v=[x[1] for x in m]
print(v)

#alterar através de indexação e slides
#alterar o valor da segunda posição
l=[1,5,6]
print(l)
l[1]=9
print(l)

#alterar dois elementos
#l[0:2] = ['abc', 25]
#print(l)

#adicionar um elemento ao final da lista
l.append('abc')
print(l)
#adicionar vários itens ao final da lista
l.extend([10,11,12])
print(l)
#remover o ultimo elemento
l.pop()
print(l)
#remover por posição
l.pop(3)
print(l)
#inverte a ordem
print(l.reverse())
#remover por conteúdo
l.remove(11)
print(l)
#ordenar a lista
abc=['zenaide','amanda','carla','luiza','bruna']
abc.sort()
print(abc)

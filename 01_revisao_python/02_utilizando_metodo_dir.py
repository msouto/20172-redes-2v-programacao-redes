#Utilizar um metodo para verificar os atributos disponiveis

#exemplos com string
x = 'spam'
#print(dir(x))
print(len(x))
print(x[0])
print(x[1:3])
print(x[-1])
print(x + ' email')

print(x.find('pa'))
print(x.upper())
print(x.isalpha())
print(x.replace('pa','ca'))

#exemplos com listas
L = [123,'casa', 3.14]
#print(dir(L))
print(len(L))
print(L[0])
#print(L*2)
print(L)
L.append('bola')
print(L)

M = [[1,2,3],[4,5,6],[7,8,9]]
print(M[0])
col2 = [n[0] for n in M]
print(col2)

#Exemplo de dicionario
D = {'com':'ABC','num':123}
print(D['num'])
D['cor'] = 'azul'
print(D['cor'])

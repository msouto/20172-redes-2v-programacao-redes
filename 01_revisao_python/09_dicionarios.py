d={'nome':'João','idade':25,'altura':''}
print(d)

print(d['nome'])
print(d['idade'])
print(len(d))

print('nome' in d)
del d['altura']
d['sexo']='masculino'
print(d)
print(len(d))

d.pop('idade')
print(d)
print(len(d))

print(d.get('idade'))
#print(d['idade'])


print(d.keys())
lista_chaves=list(d.keys())
print(lista_chaves)
print(type(lista_chaves))


for i in d.keys():
    print(i)

print(d.values())
lista_valores=list(d.values())
print(lista_valores)
print(type(lista_valores))

for i in d.values():
    print(i)

print(d.items())

arq = open('meuarquivo.txt','w')
arq.write("Olá, meu primeiro arquivo!\n")
arq.write("Fechando o arquivo\n")
arq.close()

arq = open('meuarquivo.txt','r')
texto = arq.readlines()
print(texto)

for linha in texto:
    print(linha,end='')

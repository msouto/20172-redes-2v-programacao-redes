import pickle

#gravaçã
d={'nome':'Moisés','disciplina':'programação para redes'}
arquivo=open('12_arquivo.pkl','wb')
res=pickle.dump(d,arquivo)
arquivo.close()

#Leitura
arquivo=open('12_arquivo.pkl','rb')
res=pickle.load(arquivo)
print(res)
arquivo.close()

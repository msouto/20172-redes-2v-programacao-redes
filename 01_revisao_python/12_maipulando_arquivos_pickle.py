import pickle

#gravaçã
d={'nome':'Moisés','disciplina':'programação para redes'}
arquivo=open('12_arquivo.pkl','wb')
res=pickle.dump(d,arquivo)
arquivo.close()

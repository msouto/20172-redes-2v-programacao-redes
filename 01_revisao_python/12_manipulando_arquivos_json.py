import json

#gravando arquivo em JSON
d=dict(nome='moisés',disciplina='Programação para redes')
arquivo=open('12_arquivo.json','w')
res=json.dump(d,arquivo,indent=4)
arquivo.close()

#ler o arquivo JSON
arquivo=open('12_arquivo.json','r')
res=json.load(arquivo)
print(res)
arquivo.close()

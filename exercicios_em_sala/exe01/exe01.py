#arquivo de resolucao exercicio

import random

def Arquivo():
	arquivos = []
	arquivos.append(open("nomes"))
	arquivos.append(open("temas"))
	arquivos.append(open("nomes_temas", "w"))
	return arquivos

def Sorteio(arquivo):
	nomes = [x[:-1] for x in arquivo[0]]
	temas = [x[:-1] for x in arquivo[1]]
	sorteios = []
	while len(nomes) > 0:
		escolha_nomes = random.choice(nomes)
		escolha_temas = random.choice(temas)
		escolha_sorteada = escolha_nomes + ": " + escolha_temas
		sorteios.append(escolha_sorteada)
		nomes.remove(escolha_nomes)
		temas.remove(escolha_temas)
	return sorteios

def Escrever(sorteios, arquivo):
	nomes_temas = arquivo[2]
	for x in sorteios:
		nomes_temas.write(x + "\n")

Escrever(Sorteio(Arquivo()), Arquivo())

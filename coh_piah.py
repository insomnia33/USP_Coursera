import re

def le_assinatura():

	print("Bem-vindo ao detector automático de COH-PIAH.")

	wal = float(input("Entre o tamanho medio e palavra:"))
	ttr = float(input("Entre a relação Type-Token:"))
	hlr = float(input("Entre a Razão Hapax Legomana"))
	sal = float(input("Entre o tamanho médio de sentença:"))
	sac = float(input("Entre a complexidade média da sentença:"))
	pal = float(input("Entre  tamanho medio de frase:"))

	return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
	i = 1
	textos = []
	texto = input("Digite o texto " + str(i) + "(aperte enter para sair):")
	while texto:
		textos.append(texto)
		i += 1
		texto = input("Digite o texto " + str(i) + "(aperte enter para sair):")

	return textos

def separa_sentencas(texto):
	sentencas = re.split(r'[.!?]+', texto)
	if sentencas[-1] == '':
		del sentencas[-1]
	return sentencas

def separa_frases(sentenca):
	return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
	return frase.split()

def n_palavras_unicas(lista_palavras):
	freq = dict()
	unicas = 0
	for palavra in lista_palavras:
		p = palavra.lower()
		if p in freq:
			if freq[p] == 1:
				unicas -= 1
			freq[p] += 1
		else:
			freq[p] = 1
			unicas += 1

	return unicas

def n_palavras_diferentes(lista_palavras):
	freq = dict()
	for palavra in lista_palavras:
		p = palavra.lower()
		if p in freq:
			freq[p] += 1
		else:
			freq[p] = 1

	return len(freq)

def compara_assinatura(as_a, as_b):
	pass

def calcula_assiatura(texto):
	pass

def avalia_textos(textos, ass_cp):
	pass

a = le_assinatura()
b = le_textos()
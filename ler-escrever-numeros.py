#import pytest
"Este programa pede ao usuário para que digite um número entre 0 - 999 e retorna o valor escrito por extenso. Ao final ele torna pergunta se o usuario quer digitar um novo valor."


def extenso(n,arquivo):
    ref_arquivo = open(arquivo,"r")
    for linha in ref_arquivo:
        valores = linha.split()
        if n == int(valores[0]):
           return valores[1]
    ref_arquivo.close()

def converte(n): 
	m = []
	saida = []
	string = None
	m.extend(str(n))
	if n == 0:
		return "zero"
	if n == 100:
		return "cem"
	
	multiplicador = 10 **(len(m)-1)
	for i in range(len(m)):
		saida.append(multiplicador * int(m[i]))
		multiplicador = multiplicador / 10
#	return saida
	
	if len(saida) == 3:
		string = extenso(saida[0],"arq-20-900.txt")
		if saida[1] >= 20:
			string = string + " e " + extenso(saida[1], "arq-20-900.txt")  
			
			if saida[2] > 0:
				string = string + " e " +  extenso(saida[2], "arq-1-9.txt")			
		
		m = n - saida[0]
					
		if m >= 10 and m < 20:
			string = string + " e " + extenso(m, "arq-10-19.txt")
		
		elif saida[1] == 0 and saida[2] > 0:
			string = string + " e " + extenso(saida[2], "arq-1-9.txt")	
			
	
	
	if len(saida) == 2:
	
		if saida[0] >= 20:
			string = extenso(saida[0], "arq-20-900.txt")
			if saida[1] > 0:
				string = string + " e " +  extenso(saida[1], "arq-1-9.txt")	
				
		elif n >= 10 and n < 20:
			string = extenso(n,"arq-10-19.txt")	
	
	if len(saida) == 1:
		string = extenso(n,"arq-1-9.txt")									

	return string

resposta = "s"
while resposta == "s" or resposta == "S":	
	n = int(input("Digite um valor entre 0 - 999 para que seja escrito em extenso: "))
	print("-----------------------------------------")
	print("")
	print(converte(n))
	print("")
	print("-----------------------------------------")

	resposta = input("Deseja digitar outro valor? s/n ")
	print("")
	if resposta == "n" or resposta == "N":
		print("Finalizando")
	elif resposta != "s" and "S" and "n" and "N":
		resposta = input("Deseja digitar outro valor? s/n ")
		print("")
	
	
	
	
	
	
	
	
	
	
	
#@pytest.mark.parametrize("entrada,saida",[
#	(0, "zero"),
#	(7, "sete"),
#	(10, "dez"),
#	(15, "quinze"),
#	(20, "vinte"),
#	(33, "trinta e três"),
#	(100, "cem"),
#	(300, "trezentos"),
#	(512, "quinhentos e doze"),
#	(720, "setecentos e vinte"),
#	(810, "oitocentos e dez"),
#	(999, "novecentos e noventa e nove")
#	])

#def test_converte(entrada,saida):
#	assert converte(entrada) == saida

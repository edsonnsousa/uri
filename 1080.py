def main():
	#N=input()
	vetor=[1,2,3,4,5,6,7,8,9,10]
def compara(vetor):
	menor = vetor[0]
	posicao = 0
	for i in range(1,len(vetor)):
		if vetor[i]<menor:
			menor=vetor[i]
			posicao = i
	print "Menor valor: ",valor
	print "Posicao: ",posicao

if __name__ == '__main__':
	main()
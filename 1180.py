def main():
	tamanho = input()
	vetor=[int(i) for i in raw_input().split()]


	compara(vetor)
def compara(vetor):
	menor = vetor[0]
	posicao = 0
	for i in range(1,len(vetor)):
		if vetor[i]<menor:
			menor=vetor[i]
			posicao = i
	print "Menor valor:",menor
	print "Posicao:",posicao


if __name__ == '__main__':
	main()
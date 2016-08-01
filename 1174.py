def main():
	listar()
def listar():
	numeros=[]
	for i in range(0,100):
		num = input()
		numeros.append(num)
		if num<=10:
			print "A[%d] = %.1f"%(i,numeros[i])

if __name__ == '__main__':
	main()

#Ex4 Faça um programa que receba dois números inteiros do usuário n1 e n2, de modo que n1 < n2. Crie uma função que imprime os números de n1 a n2 na ordem inversa.
def imprimir (x1,x2):
	for i in range(x2,x1-1,-1):
		print(i)

def main():
	n1 = int(input("Digite o primeiro valor: "))
	n2 = int(input("Digite o segundo valor(deve ser maior que o primeiro: "))
	imprimir(n1,n2)

main()

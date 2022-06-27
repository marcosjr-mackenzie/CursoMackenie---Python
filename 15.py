#Ex3 Faça um programa que recebe um número digitado pelo usuário. A função retorna o valor de caractere ‘P’, se o número for positivo, e ‘N’, se o número for zero ou negativo.
def sinal(n):
	if n>0:
		print("P")
	else:
		print("N")

def main():
	x = int(input("Digite um número: "))
	sinal (x)
		
main()
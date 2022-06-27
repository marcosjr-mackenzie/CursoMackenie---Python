#Ex1 Faça um programa que receba dois números, soma e mostra o resultado da soma. Crie a função main() para receber as entradas e a função soma para calcular a soma.

def soma(x1,x2):
    soma = x1+x2
    return soma

def main():
	n1 = int(input("Número 1: "))
	n2 = int(input("Número 2: "))
	resultado = soma(n1, n2)
	print ("O resultado da soma de",n1, "e", n2, "é:", resultado)

main()







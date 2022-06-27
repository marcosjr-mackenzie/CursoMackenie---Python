#Ex6. Escreva uma função que, dado o valor da conta de um restaurante, calcule e exiba a gorjeta do garçom, considerando 10% do valor da conta.

def gorjeta (n):
	gorjeta = n/10
	return gorjeta

def main():
	conta = int(input("Digite o valor da conta: "))
	resultado = gorjeta(conta)
	print("Você deve dar", resultado, "reais de gorjeta ao garçomte")

main()
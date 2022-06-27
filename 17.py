#Ex5. Faça uma função que computa a potência ab para valores a e b (assuma números inteiros) passados por parâmetro (não use o operador **).

import math
def potencia(x1,x2):
	potencia = math.pow(x1,x2)
	return potencia

def main():
	a = int(input("Digite o valor de a(base): "))
	b = int(input("Digite o valor de b(expoente): "))
	resultado = potencia(a, b)
	print("O resultado de",a,"elevado a",b,"é:", resultado)

main()
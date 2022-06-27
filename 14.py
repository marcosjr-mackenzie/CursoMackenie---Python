#Ex2 Faça um programa que recebe um número do usuário, calcula e mostra o fatorial desse número. Crie a função calculaFatorial

def calculaFatorial(n):
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n - 1
    return fatorial
        
def main():
	x = int(input("Deseja calcular o fatorial de qual número: "))
	resultado = calculaFatorial(x)
	print(resultado)
	
main()
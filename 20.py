print('Escolha uma opção: \n [1] - converter de binário / octal / hexadecimal para decimal \n [2] - converter decimal para binário / octal / hexadecimal \n [3] - Informações do grupo \n [4] - Sair ')
print(" ")
opcao = int(input("Digite uma opção: "))
print(" ")

#OPÇÃO 1 -----------------

if opcao == 1:
	base = int(input("Informe a base (2, 8 ou 16): "))
	if base == 2:
		num = (input("Digite o número binário a ser convertido: "))
		bin = int(num, 2)
		print("\n{} convertido para decimal é igual a {}".format(num, bin))
	
	elif base == 8:
		num = (input("Digite o número octal a ser convertido: "))
		oct = int(num, 8)
		print("\n{} convertido para decimal é igual a {}".format(num, oct))

	elif base == 16:
		num = input("Digite o número hexadecimal a ser convertido: ")
		hex = int(num, 16)
		print("\n{} convertido para decimal é igual a {}".format(num, hex))
		
#OPÇÃO 2 -----------------

elif opcao == 2:
	num = int(input("Digite o número decimal a ser convertido: "))
	base = int(input("Informe a base do número digitado (2, 8 ou 16): "))
	if base == 2:
		print("\n{} convertido para BINÁRIO é igual a {}".format(num, bin(num)[2:]))
		
	elif base == 8:
		print("\n{} convertido para OCTAL é igual a {}".format(num, oct(num)[2:]))
		
	elif base == 16:
		print("\n{} convertido para HEXADECIMAL é igual a {}".format(num, hex(num)[2:]))
		
	else:
		print("\nBase inválida")
		
#OPÇÃO 3 -----------------
		
elif opcao == 3:
	print ("Informações do grupo: \n \n Marcos Carvalho Corrêa Junior - TIA: 32234120 \n Leonardo Binder - TIA: 32244681")

#OPÇÃO 4 -----------------

elif opcao == 4:
	print("ADEUS")
	print(" ")



																															
		
	



x = int(input("Insira o peso do peixe: "))
if x>50:
	y = 4*(x-50)
	print ("O peso excedente é de ",x,"portanto deve pagar",y, "reais de multa")
else: print("Dentro do regulamento")

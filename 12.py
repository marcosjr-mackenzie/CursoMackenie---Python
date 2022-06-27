import random 
contapar = 0
contaimpar = 0
contaprimo = 0
y = 0
x = 0
contatotal = 0

while contatotal < 10:
	contatotal = contatotal + 1
	x = random.randint(1, 100)
	if x%2 == 0:
		contapar = contapar + 1
	else:
		contaimpar = contaimpar + 1
	print ("Numéro",contatotal,":",x)
	for i in range(2,x):
		if x%i == 0:
			y = y + 1
			contaprimo = (10 - y)
			break

print ("O total de números pares sorteados é:", contapar)
print ("O total de números ímpares sorteados é:", contaimpar)
print("O total de números primos sorteados é:", contaprimo)

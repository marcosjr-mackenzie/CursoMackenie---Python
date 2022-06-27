idade = int(input())
peso = float(input())
genero = input()
if genero == "M" or "m":
	genero = 1
elif genero == "F" or "f":
	genero = 0




if idade > 12 and peso >= 60 and genero == 1:
	print ("1000")
elif idade > 12 and peso >= 60 and genero == 0:
	print ("500")
elif idade > 12 and peso < 60 and genero ==1:
	print ("875")
elif idade > 12 and peso < 60 and genero ==0: 
	print ("437,5")
elif idade < 12 and peso > 5 and peso < 9 and genero ==1:
	print ("125")
elif idade < 12 and peso > 5 and peso < 9 and genero ==0:
	print ("62,5")
elif idade < 12 and peso > 9 and peso < 16 and genero ==1:
	print ("250")
elif idade < 12 and peso > 9 and peso < 16 and genero ==0:
	print ("125")
elif idade < 12 and peso > 16 and peso < 24 and genero ==1:
	print ("375")
elif idade < 12 and peso > 16 and peso < 24 and genero ==0:
	print ("187,5")
elif idade < 12 and peso > 24 and peso < 30 and genero ==1:
	print ("500")
elif idade < 12 and peso > 24 and peso < 30 and genero ==0:
	print ("")



etiqueta = float(input())
código = int(input())
if código == 1:
	final = etiqueta*0.9
	print ("NO BOLETO COM 10% DE DESCONTO")
elif código == 2:
	final = etiqueta*0.95
	print ("NO CARTAO COM 5% DE DESCONTO")
elif código == 3:
	final = etiqueta
	print ("EM DUAS VEZES SEM DESCONTO")
elif código == 4:
	final = etiqueta*1.1
	print ("EM TRES VEZES COM ACRESCIMO DE 10%")
print (final)
	
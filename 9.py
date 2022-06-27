km = float(input())
gasolina = int(input())
kml = km/gasolina
print (kml)
if kml < 8:
	print ("VENDA O CARRO")
elif kml >= 8 and kml <= 12:
	print ("CARRO ECONÔMICO")
elif kml > 12:
	print ("CARRO SUPER ECONÔMICO")
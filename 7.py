etiqueta = float(input())
código = int(input())

if código == 1:
	final = etiqueta*0.9
elif código == 2:
	final = etiqueta*0.95
elif código == 3:
	final = etiqueta
elif código ==4:
	final = etiqueta*1.1

final = round(final, 2)

print (final)

	


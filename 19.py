contmaiorIdade = 0
contmenorIdade = 0
cont65 = 0
contM1835 = 0
contporcentagem1835 = 0
contporcentagem65 = 0
totalpessoas = 0

idade = int(input("Idade: "))

while idade != -1:
	sexo = input("Sexo (M ou F)")
	totalpessoas += 1
	if idade >= 18 and idade <= 35 and sexo == "F":
		contM1835 += 1 
	elif idade >= 65:
		cont65 +=1
	if idade > contmaiorIdade:
		contmaiorIdade = idade
	if contmenorIdade == 0 or contmenorIdade > idade:
		contmenorIdade = idade
	idade = int(input("Idade: "))
	
contporcentagem1835 = (contM1835*100)/totalpessoas
contporcentagem65 = (cont65*100)/totalpessoas
	
print	(contmaiorIdade, "é a maior idade entre os habitantes desta pesquisa")
print (contmenorIdade, "é a menor idade entre os habitantes desta pesquisa")
print ("o percentual de indivíduos do sexo feminino com idade entre 18 e 35 anos é de ", contporcentagem1835, "%" )
print ("o percentual de indivíduos com idade maior ou igual a 65 é igual a", contporcentagem65, "%" )
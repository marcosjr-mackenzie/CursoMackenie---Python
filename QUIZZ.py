gabarito = []
assinaladas = []
pontos = []
i = "S"

def questao (pergunta,a,b,c):
   print(pergunta)
   print(" ")
   print(a)
   print(b)
   print(c)
   print(" ")


def acerto (correta, corretaminiscula, explicacao):
   x = input("Digite a alternativa correta (A, B ou C): ")
   if x == correta or x == corretaminiscula:
      pontos.append(1)
      print(" ")
      print ("Parabéns você acertou, próxima questão ->")
   else:
      print(" ")
      y = input("Você errou, deseja ver a explicação (S ou N)?: ")
      if y == "S" or y == "s":
         print (explicacao)
   gabarito.append(correta)
   assinaladas.append(x)
   print(" ")
   print("################################################################################################################################################")

#CABEÇALHO--------------------------------------------------------------------

print(" ")
print("################################################################################################################################################")
print(" ")
print("               ALGORITMOS E PROGRAMAÇÃO")
print("                   QUIZ MATEMÁTICO")
print("                      TURMA 01N")
print(" ")
print("Nome: Pedro Almeida Gonçalves TIA: 32268629")
print("Nome: Marcos Carvalho Correa Junior TIA: 32234120")
print("Nome: Bruno Roveri Custódio TIA: 32231911")
print(" ")
print("################################################################################################################################################")
   

while i == "S" or i == "s":

        #Questão 1--------------------------------------------------------------------

   print(" ")
   print("QUESTÃO 1 ->")
   questao ("Questão 1: Complete a sequência corretamente: 1,2,3,5,6,7,9,10,11,..., ", "A) 13, 14, 15", "B) 12, 13, 14", "C) 14, 13, 12")
   acerto ("A","a","Como vimos, a sequência é de 3 números seguidos e depois pula 1, como estava 9,10,11 tinha que pular o 12 e seguir com 13,14,15")
   
   #Questão 2-------------------------------------------------------------------
   
   print(" ")
   print("QUESTÃO 2 ->")
   questao ("Em qual alternativa há três oitos, três zero?", "A) 3830", "B)88800", "C)88830",)
   acerto ("C","c","Dizer “três oitos” é o mesmo que 888. Repare que a palavra “oito” está no plural na primeira opção, e no singular na segunda. Da mesma forma, dizer “três zero” é o mesmo que 30. É diferente de dizer “três zeros”, que é o mesmo que 000")
   
   #Questão 3-------------------------------------------------------------------
   
   print(" ")
   print("QUESTÃO 3 ->")
   questao ("Maria comprou um vaso de flores por 20 reais e o vendeu por 25 reais. Arrependida da venda, comprou o mesmo vaso por 35 reais, mas logo decidiu vendê-lo por 40 reais. No final, quanto ela lucrou? ", "A) 5 reais", "B) 10 reais", "C) 15 reais")
   acerto ("B","b","Maria gastou 20 reais e depois mais 35, o que soma 55 reais. Por sua vez, Maria recebeu primeiro 25 reais e depois mais 40, somando 65 reais. 65 - 55 = 10 reais.")
   
   #Questão 4-------------------------------------------------------------------
   
   print(" ")
   print("QUESTÃO 4 ->")
   print(" ")
   print("0 + 7 = 7")
   print("2 + 8 = 17")
   print("2 + 9 = 28")
   print("5 + 17 = ?")
   print(" ")
   print("A) 50")
   print("B) 22")
   print("C) 90")
   print(" ")
   acerto("A","a","O resultado 50 é obtido quando você soma o resultado da linha de cima com a conta da linha de baixo: 0 + 7 = 0; 8+2+7 = 17; 2+9+17 = 28; 5+17+28 = 50.")
   
   #Questão 5-------------------------------------------------------------------
   print(" ")
   print("QUESTÃO 5 ->")
   questao("Quatro amigos se reuniram. Carlos tem a metade da idade de Matheus mais 2 anos. Henrique tem 8 anos. Matheus tem a idade de Henrique mais a metade de sua idade. Paulo tem a metade da idade de Carlos mais a metade da idade de Henrique. Qual dos amigos é o mais velho?", "A) Paulo", "B) Henrique", "C) Matheus")
   acerto("C","c", "Henrique tem 8 anos. Matheus tem a idade de Henrique, 8, mais metade de sua idade, que é 4. Logo, 8 + 4 = 12 anos. Carlos tem a metade de 12, que é 6, mais 2. Temos que 6 + 2 = 8. Carlos tem 8 anos. Paulo tem aetade da idade de Carlos, que é 4, mais a metade da idade de Henrique, que também é 4. Logo Paulo tem 8. Portanto, Matheus é o mais velho com 12 anos.")
   
   #Questão 6-------------------------------------------------------------------
   
   print(" ")
   print("QUESTÃO 6 ->")
   questao("Ana teve 5 filhas. A primeira chama-se Segunda, A segunda chama-se Terça, A terceira chama-se Quarta, A quarta chama-se Quinta. Qual é o nome da quinta.","A) Quinta", "B) Qual","C) Sexta")
   acerto("B","b", "A quinta filha chama-se Qual, tal como está escrito na última frase, em que consta essa afirmação. Repare que a última frase não é uma pergunta.")
   
   #Questão 7-------------------------------------------------------------------
   
   print(" ")
   print("QUESTÃO 7 ->")
   questao("Um pequeno caminhão pode carregar 50 sacos de areia ou 400 tijolos. Se foram colocados no caminhão 32 sacos de areia, quantos tijolos pode ainda ele carregar? ","A) 350","B)130","C)144")
   acerto("C","c", "1 saco de areia = 8 tijolos (400 tijolos / 50 sacos = 8) Se o caminhão carregou 32 sacos de areia, ainda tem espaço para 18 sacos, mas em vez de sacos, quer levar tijolos, ou seja 18 . 8 = 144.")
   
   #Questão 8-------------------------------------------------------------------
   
   print(" ")
   print("QUESTÃO 8 ->")
   questao("Bruna tem 54 anos e sua mãe, Dona Amélia, tem 80. Há quantos anos a idade de Dona Amélia era 3 vezes a idade de Bruna?","A) 41 anos","B) 37 anos","C) 53 anos")
   acerto("A","a","Pegamos a diferença que é de 36 anos, logo em seguida precisamos pegar as alternativas e subtraímos pela idade da Dona Amélia, pegando o resultado que é 39 se divide por 3, dando certo dará 13.")
   
   #Questão 9-------------------------------------------------------------------
   
   print(" ")
   print("QUESTÃO 9 ->")
   questao("Uma mulher irá ter um bebê. Se ele for menino, ficará faltando apenas um filho para que o número de meninos seja igual ao de filhas. No entanto, se o bebê for uma menina, o número de filhas da mulher será o dobro do número de meninos. Quantos filhos ela tem e qual é o sexo deles?","A) 4 filhos– 3 meninas e 1 menino", "B) 8 filhos– 5 meninas e 3 meninos","C) 9 filhos – 6 meninas e 3 meninos")
   acerto("B","b","Assim, se tiver mais 1 menino faltará apenas mais 1 para ter o mesmo número de filhos e filhas, num total de 10. Se tiver mais 1 menina, serão 6 filhas ao todo, que é o dobro dos 3 filhos que ela já tem")
   
   #Questão 10-------------------------------------------------------------------
   
   print(" ")
   print("QUESTÃO 10 ->")
   questao("No ônibus que entrei havia 8 passageiros. Pouco depois, 3 pessoas desceram e duas entraram. Quantas pessoas há no táxi?", "A) 8 pessoas", "B) 6 pessoas","C) 9 pessoas)")
   acerto("C","c", "Quando eu entrei no táxi, o táxi ficou com 10 pessoas contando o motorista. Com a saída de 3, ficaram 7, mas 2 entraram, ou seja, ficaram 9.")

   #CONCLUSÃO-------------------------------------------------------------------
   
   print(" ")
   print ("Suas respostas: ", assinaladas)
   print ("Gabarito: ","     " ,gabarito)
   print(" ")
   print("SUA PONTUAÇÃO: ", sum(pontos))
   print(" ")
   
   i = input("Quer refazer o QUIZ (S ou N)?: ")
   if i == "S" or i == "s":
      gabarito.clear()
      assinaladas.clear()
      pontos.clear()
   
print(" ")
print ("MUITO OBRIGADO POR REALIZAR NOSSO QUIZ, ATÉ A PRÓXIMA")
print("################################################################################################################################################")


'''
Desafio - crie uma lista de frutas e outras de vegetais, use um for loop aninhado (nested) para imprimir na tela todas as combinações possiveis de frutas e vegetais.
Em primeiro lugar deve aparecer as frutas e em segundo os vegetais.

'''

frutas = ["maça", "banana", "melancia"]

vegetais = ["alface", "repolho", "tomate"]

for fruta in frutas:
	for vegetal in vegetais:
		print(fruta, vegetal)


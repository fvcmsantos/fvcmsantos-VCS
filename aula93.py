'''
Desafio - crie uma lista de frutas que inclui maçã tres vezes e outras frutas de sua escla. Use o loop for para contar quantas veze maçã aparece na lista e imprima o resultado.	
'''

frutas = ["maça", "banana", "maça", "maça", "uva", "maça", "melancia", "maça"]

contador = 0

for fruta in frutas:
	if fruta == "maça":
		contador += 1

print(f'A fruta maça aparece {contador} vezes na lista')


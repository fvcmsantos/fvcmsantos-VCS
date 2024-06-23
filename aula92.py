	
'''
Desafio  - crie um loop que imprima os numeros pares de 1 a 10, mas pare de imprimir assim que chegar no numero 5, usando comando break. 
Depois crie um segundo loop que imprima os numeros de 1 a 10, mas pule a impressao do numero 5, usando o comando continue.
'''

for numero in range(1, 11):
	if numero == 5:
		break
	print(numero)

print('---------------------')

for numero in range(1, 11):
	if numero == 5:
		continue

	print(numero)


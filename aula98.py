'''
Desafio - crie uma lista de numeros de 1 a 10. Use o for loop para interar sobre a lista. Se o numero atual da interação for par, imprima: 'O numero atual da interação é par', caso contrario, imprima: 'O numero atual da interação é impar'

# Consider this snippet from ./aula99.py


for loop in range(1, 11):
	if loop % 2 == 0:
		print(f'O numero {loop} é par')

	else:
		print(f'O numero {loop} é impar')

		'''

# ou

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]

for numero in numeros:
	if numero % 2 == 0:

		# % 2, significa que o numero é divisivel por 2, logo se não tiver resto, é par.
		
		print(f'O numero {numero} é par')

else:
	print(f'O numero {numero} é impar')
	




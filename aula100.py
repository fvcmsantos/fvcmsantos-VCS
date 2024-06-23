'''
Desagio - crie uma lista com 5 nome de paises e as suas capitais, peça para o usuario digitar o nome de um pais, se o pais estiver na lista, imprima: 'A capital do [pais] é a [capital]', caso contrario, imprima: 'O pais não está na lista.
'''

paises = ['Brasil', 'Argentina', 'Chile', 'Uruguai']

capitais = ['Brasilia', 'Buenos Aires', 'Santiago', 'Montivideo']

pais = input('Digite o nome de um pais: ')

if pais in paises:
	print(f'A capital do {pais} é a {capitais[paises.index(pais)]}')

else:
	print('O pais não está na lista')

	
					
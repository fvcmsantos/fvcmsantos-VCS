'''
crie uma lista com o nome de tres cidades, peça parao usuario digitar o nome de uma cidade, se a cidade estiver na lista, imprima: 'A cidade está na lista das cidades', caso contrario, imprima: 'A cidade não está na lista das cidades'
'''

cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']

cidade = input('Digite o nome de uma cidade: ')

if cidade in cidades:

	print('A cidade está na lista das cidades')

else:
	print('A cidade não está na lista das cidades')



	
'''
Desafio - imagine que voce tem uma loja de carros, crie uma lista com os carros que voce tem em estoque: BMW X6, BMW i5, BMW i8, BMW i4.
Peça para o usuario insira o nome do carro que ele deseja comprar, se o carro estiver em estoque, imprima: 'carro disponivel', caso contrario, imprima: 'carro indisponivel'

'''

lista_carros = ['BMW X6', 'BMW i5', 'BMW i8' , 'BMW i4']

carro = input('Digite o nome do carro que deseja comprar: ')

if carro in lista_carros:
	print('Carro disponivel')

else:
	print('Carro indisponivel')
	

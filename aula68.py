# Try/Except lidando com o input errado do usuario (erro de paramentros, por exemplo, o pedido é uma string(letra) e o usuario digita um interger (numero))


try:
	
	valor = int(input('Digite o valor do seu produto:  '))

	print(valor)

except ValueError:
		print('Por favor digitar somente valores numericos')


#usando esta função, o programa não para de rodar, mas avisa o usuario que o valor digitado não é um numero.




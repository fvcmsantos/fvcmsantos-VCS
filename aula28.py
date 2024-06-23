# Conteudo HEX - significa que não sabemos quantos argumentos vai receber, mas sabemos que vai receber um argumento

# *args - argumentos
# xargs = vários argumentos

# criar uma função que soma ários numeros

def multiplicação(*numeros):
	resultado = 1
	for num in numeros:
		resultado *= num
	return resultado


# em resultado = necessario indicar que tipo de conta voce precisa => += (soma); *= (multiplica), /= (divide).

	
	# quando usamos o * signiica que podemos adicionar vários argumentos (neste caso numeros)

x= multiplicação(2,3,4,7)


print(x)

'''
Vamos fazer a conta de multiplicação no papel. Para isso, utilizaremos os números 2, 3, 4 e 7.

Comece escrevendo os números na ordem em que aparecem: 2, 3, 4 e 7.

Multiplique esses números um por um:

2 × 3 = 6
6 × 4 = 24
24 × 7 = 168
Portanto, o resultado da multiplicação dos números 2, 3, 4 e 7 é 168.
'''



	

	

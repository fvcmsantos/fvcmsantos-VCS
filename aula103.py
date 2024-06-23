'''
Desafio => As funções recursivas são funções que se chama dentro do seu próprio código. Elas sao utis para resolver problemas que podem ser divididos em subproblemas menores ou de natureza semelhantes.

Um exemplo classico de onte a recursão é usada é o calculo do fatorial de um numero. O fatorial de um numero n é o produto de todos os numeros de 1 a n.
'''

# exemplo de fatorial
# 5! = 5 * 4 * 3 * 2 * 1

def fatorial(n):
		if n == 0 or n == 1:
			return 1

		else:
				return n * fatorial(n-1)

numero_do_usuario = int(input('Digite um numero: '))

print(f' O fatorial de {numero_do_usuario} é {fatorial(numero_do_usuario)}')









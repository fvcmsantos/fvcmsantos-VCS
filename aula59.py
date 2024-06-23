# Lambda - função anônima, usada para executar uma função sem nome e sem definição

#Usada para simpliciar as funções

def somar(x):
	func2 = lambda x: x + 10
	return func2(x) * 4

print(somar(2))

# Função lambda dentro de outra função


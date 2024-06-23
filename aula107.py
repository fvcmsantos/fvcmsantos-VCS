''''
Desafio - crie um funcao lambda que eleve um numero ao quadrado (**) e use essa fnção para calcular o quadrado de todos os numeros em uma lista usando a funcao loop for
'''

numeros = [1,2,3,4,5,6,7]
quadrado = lambda num: num ** 2

resultado = []
for i in numeros:
		resultado.append(quadrado(i)) 
	#append = adicionar

print(f'Os quadrados dos numeros {numeros} são {resultado}')
	
	#1 ULTIMA AULA SOBRE PROGRAMAÇÃO EM PYTHON
	#2 REVEJA TODO O CONTEUDO E REFAÇA TODOS OS EXERCICIOS
	#3 ALGUNS ERROS DE DIGITAÇÃO, NAO SÃO DE PROPOSITO
	
	



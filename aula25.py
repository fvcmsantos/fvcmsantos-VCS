#Parametros e argunmentos de uma função - usado para aumentar a legibilidade do codigo.	

''''
def boas_vindas_Marcos():
	print('ola Caio!')
print('temos 5 notebooks em estoque')

def boas_vindas_Ronaldo():
	print('ola Caio!')
print('temos 5 notebooks em estoque')

def boas_vindas_Linda():
	print('ola Caio!')
print('temos 5 notebooks em estoque')

boas_vindas_Marcos
boas_vindas_Ronaldo
boas_vindas_Linda
'''

#onde nome e quantidade são PARAMETROS e a função (neste casos "boas_vindas") é o ARGUMENTO."


def boas_vindas(nome, quantidade):
	print(f'ola {nome}.')
	print(f'temos {str(quantidade)}  notebooks em estoque')


# e neste caso o "boas_vindas" é o ARGUMENTO:

boas_vindas("Marcos", 5)
boas_vindas("Ronaldo", 4)
boas_vindas("Linda", 2)

# Perceba que o proprio sistema usa o argumento e coloca o total em estoque correto.











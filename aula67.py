#Trabalhando com try e except com uma lista

# Usado para testar erros

# Faz a leitura e escrita de arquivos

# Abrir um arquivo

try:
	letras = ['a', 'b', 'c']
	print(letras[3])

except IndexError:
	print('Index não existe')

#neste caso, como estou pedindo uma informação que nao existe, vai dar erro.

# neste caso pedimos o index 3, que nao existe na lista








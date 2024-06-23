# Função Filter
# usado para filtrar elementos de uma lista

valores = [10, 12, 34, 44, 57]

def remover20(x):
		return x > 20

print(list(filter(remover20, valores)))

#outra forma de fazer:
print(list(filter(lambda x: x > 20, valores)))

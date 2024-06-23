# Lista and Genarator Expressions	

# Uma forma mais rápida para listas, dicionários e etc
# Menos memória alocada
# Valores em bytes	

from sys import getsizeof


numeros = [x * 10 for x in range(100)]
print(getsizeof(numeros))

print('=======')

numeros = (x * 10 for x in range(100))
print(type(numeros))
print(getsizeof(numeros))

#trabalhando arrays 
#similar a listas
#quando devo usar uma arrays? dependende do tamanho da lista.
#quando a lista for muito grande

#nao está disponivel, precisa ser importada
# import numpy as np

from array import array


letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]


#type code: 
# 'u' -> unicode character (string)
# 'i' -> signed integer (integral)
# 'f' -> float (casas decimais)
# 'd' -> double (casa decimal, mais prcisa)

letras = array('u', ['a', 'b', 'c', 'd'])
numeros_i = array('i', [10, 20, 30, 40])
numeros_f = array('f', [1.2, 2.2, 3.2])

print(letras)
print(numeros_i)
print(numeros_f)



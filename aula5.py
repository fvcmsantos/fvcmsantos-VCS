# Entendendo o slice (serve para pegar apenas partes de uma variavel que precisa trabalhar)
# index = posição de uma variável (do zero em diante)
#ABACATE = INDEX (0,1,2,3,4,5,6), onde 
# A = 0, 
# B = 1, 
# A = 2
#...

fruta = "Abacate"
#index = 012346

print(fruta[0:7]) # no python para obter uma lista completa que necessita, é necessário incluir sempre um número a mais. Exemplo: se a base tem 6 dados, entao precisa indicar um range de 0-7 (exemplo acima)

valor = 99.75
#index 01234
valor = str(valor)

print(valor[0:2])
print(valor[3:5])
print(valor[4])





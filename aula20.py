# while loops - usado quando precisamos verificar se algo está dentro de uma lista.
# usado para loops dependentes de uma condição
#desafio: criar uma promoção de um produto no valor de R$ 100,00 

valor = 100
dia = 0
while valor > 20:
   dia += 1
   print(f' no dia {dia} o produto vai ser vendido por R$ {valor}')
   valor -= 5

#neste exemplo o valor vai ate 25,00, pois o valor de 20,00 não atende a condição.

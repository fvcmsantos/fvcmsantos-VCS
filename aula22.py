# if e else = roda apenas uma vez (verdadeiro ou falo)
#for loop = precisa dizer quantas vezes voce precisa rodar 
#While = loop condicional, vai rodar até chegar no ponto definido pelo usuario.

#exemplo: loja virual que vende produtos de terceiros (mercado livre)

#Publicar um produto com uma comisao de 10% se for acima de R$ 20,00

valor = int(input('Digite o valor do seu produto R$ '))

while valor > 20:
    valor = (valor * 0.10) + valor
    print(f'O valor do seu produto será de R$ {valor}')
    break

# se o loop entrar no infinito, use o BREAK para parar o loop.

  




                  


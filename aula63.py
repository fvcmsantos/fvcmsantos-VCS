# Entendendo List Comprehesion com Strings

# utilizado quando voce precisa criar uma nova lista a partir de uma existente

# [expressao for iten in itens]


frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']

#selecionar apenas frutas quem contem a letra B

frutas2 = [iten for iten in frutas1 if 'b' in iten]

#traduzindo: para os item da lista, pegue apenas frutas com a letra b

print(frutas2)



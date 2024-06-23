#armazenando mais de uma informação em variaveis
#manter a sequencia dos dados em uma variavel

cidade1= 'São Paulo'
cidade3= 'Salvador'
cidade3= 'Rio de Janeiro'

cidades = ['São Paulo', 'Rio de Janeiro', 'Salvador', 'Goiania']

cidades.append('Santa Catarina')

# o append, inclui outras informações em sua lista

cidades.remove('Salvador')
# o remove, exclui o nome pedido da lista

cidades.insert(0, 'Santa Catarina')

# o insert, insere um nome na lista, mas no lugar que você pedir.


cidades.pop(0)
# o pop, exclui o nome que você pedir, mas no lugar que você pedir.	(neste caso pedimos para excluir Santa Catarina))

cidades.sort()
# o sort, coloca a lista em ordem alfabetica

print(cidades)



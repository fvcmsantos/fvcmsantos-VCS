#looping dentro de um dicionario

aluno = {'nome': 'Ana', 'idade': 16, 'nota_final' : 'A', 'aprovação': True}

for x in aluno.items():
	print(x)

for keys, values in aluno.items():
	print(keys, values)

#se usar apenas o for x, o resultado sera apenas as strings e nao as informações sobre cada item.
#neste caso recomenda-se usar a keys e values para mostrar as informações de cada item.


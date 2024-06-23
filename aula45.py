#cores = deixando a digitação do usuario padrao, para nao ter problemas de escrever com letra maiuscula (upper) ou minuscula (lower)

cor_cliente = input('Digite a cor dejada: ')
cores = ['amarelo', 'azul','verde', 'azul',	'vermelha' ]

if cor_cliente.lower() in cores:
		print('Temos em estoque')
else:
		print('Não temos esta cor em estoque')	

# argumentos e não argumentos - default and non defaut - usado para o caso de não informar o argumento na hora da chamada da função.	


#def boas_vindas(nome, quantidade):
		#print(f'ola {nome}.')
		#print(f'temos {str(quantidade)}  notebooks em estoque')"

#boas_vindas('marcos,')"

#neste caso vai dar erro, pois nao informamos a quantidade.

''''''
#a quantidade de argumentos e de paramentros devem ser o mesmo e quando isso não é possivel, devemos usar o default ou non default

#Para resolver esta situação, basta reescrever a funçao, atribuindo um valor defaul para a quantidade (6).


def boas_vindas(nome, quantidade=6):
		print(f'ola {nome}.')
		print(f'temos {str(quantidade)}  notebooks em estoque')

boas_vindas('marcos')

#defaut and non default precisa entrar sempre em ordem.

#o argumento que voce NAO define o valor (non default), deve sempre vir em primeiro lugar








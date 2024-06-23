# Classes e objetos

# Constructors - usados para criar objetos

class Funcionarios:
		def __init__(self, nome, sobrenome, data_nascimento):

			self.nome = nome
			self.sobrenome = sobrenome			 
			self.data_nascimento = data_nascimento

# self pega cada objeto (neste  caso usuario) e atribui a ele os valores passados no construtor
			

#criar o objeto usuario1 = Funcionarios('Mariana' 'Costa', '12/01/2009')
usuario1 = Funcionarios('Caio', 'Costa', '12/01/1998')

usuario2 = Funcionarios('Mariana', 'Costa', '12/01/2000')

usuario3 = Funcionarios('Bubble', 'Thomaz', '12/01/2018')


print
print(usuario1.nome)
print(usuario2.nome)
print(usuario3.nome)




# Classes e objetos

class Funcionarios:
	def __init__(self, nome, sobrenome, data_nascimento):

		self.nome = nome
		self.sobrenome = sobrenome			 
		self.data_nascimento = data_nascimento

	def nome_completo(self):
			return self.nome + ' ' + self.sobrenome


usuario1 = Funcionarios('Caio', 'Costa', '12/01/1998')

usuario2 = Funcionarios('Mariana', 'Costa', '12/01/2000')

usuario3 = Funcionarios('Bubble', 'Thomaz', '12/01/2018')


print
print(usuario1.nome_completo())
print(usuario2.nome_completo())
print(usuario3.nome_completo())

# ou forma mais simples para chamar a função

print(Funcionarios.nome_completo(usuario1))



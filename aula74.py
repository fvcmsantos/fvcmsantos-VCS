#classes e objetos

from datetime import datetime


class Funcionarios:
	def __init__(self, nome, sobrenome, ano_nascimento):

		self.nome = nome
		self.sobrenome = sobrenome			 
		self.data_nascimento = ano_nascimento

	def nome_completo(self):
			return self.nome + ' ' + self.sobrenome

	def idade_funcionario(self):
		ano_atual = datetime.now().year
		self.data_nascimento = int(ano_atual - self.data_nascimento)
		return self.data_nascimento


		
		
usuario1 = Funcionarios('Caio', 'Costa', 2005)

usuario2 = Funcionarios('Mariana', 'Costa', 2000)

usuario3 = Funcionarios('Bubble', 'Thomaz', 1998)



print(Funcionarios.idade_funcionario(usuario1))

print(Funcionarios.idade_funcionario(usuario2))

print(Funcionarios.idade_funcionario(usuario3))
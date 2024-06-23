#functions (funçõe) - realizam uma tarefa ou calcula e retorna um valor
# DRY - Don't repeat yourself quer dizer não se repita
def cliente1(nome):
	print(f'Olá {nome}')


# por esta função o cliente1 não vai imprimir nada pois não foi chamado, mas se eu chamar a função cliente1 e colocar o nome Mariana, ela vai imprimir a mensagem - ISSO É UMA TAREFA, POIS IMPRIMIU, MAS NAO ARMAZENOU NADA.


def cliente2(nome):
	return f'Olá {nome}'

x = cliente1('Maria')
y = cliente2('Caio')

print(y)

# SE voce quer so uma tarefa = use print
#se precisa usar e outra coisa = use return (outra calculo função etc)








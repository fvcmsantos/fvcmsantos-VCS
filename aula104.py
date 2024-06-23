'''
Desafio => A primeira função deve aceitar um numero e retornar o dobro desse numero. A segunda função deve aceitar um numero e retornar o quadrado desse numero. Em seguida, chame a primeira função dentro da segunda função  para retornar o o dobro de um numero.
'''

def dobro(numero):
		return numero * 2

def quadrado(numero):
		return dobro(numero) ** 2
# um funcao chamando outra funcao

numero_do_usuario = int(input('Digite um numero: '))

print(f' O quadrado do dobro de um numero {numero_do_usuario} é {quadrado(numero_do_usuario)}')


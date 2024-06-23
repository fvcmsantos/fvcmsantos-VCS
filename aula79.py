# desafios com funções

'''
criar um programa que calcula a quantidade de tinta necessaria para pintar uma parede.

informações: rendimento, altura e largura (variaveis e ser criada)

Depois criar uma função que calcula a quantidade de latas de tinta necessaria para pintar a parede.

o programa deve mostrar na tela a mensagem: 'voce necessita de x latas de tinta'
'''

#usa int = numero inteiro
rendimento = int(input('Qual o rendimento da lata? '))

altura = int(input('Qual a altura da parede? '))

largura = int(input('Qual a largura da parede? '))

#definicao de função:
def calculo_tinta():
	area = altura * largura
	
	total_latas = area / rendimento
	
	print(f'Voce precisa de {total_latas} latas de tinta')



calculo_tinta() #função definida no inicio





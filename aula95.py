'''
Desafio - Crie um programa em que pede para o usuario digitar uma idade, se a idade digitada for menor que 13 anos, imprima: 'voce é uma criança', se a idade for 19 anos, o sistema deve responder: 'voce é um adolescente' e se for maior ou igual a 20, diga: 'voce é um adulto'

'''
idade = int(input('Digite sua idade: '))
if idade < 13:
	print('Você é uma criança')

elif idade < 20:
	print('Você é um adolescente')

else:
	print('Você é um adulto')




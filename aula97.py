'''
Crie um loop que peça para o usuario digitaR o nome de uma fruta, se a fruta digitada nao for  ABACATE, o loop deve continuar pedindo ao usuario digitar o nome de outra fruta. Quando o usuario digitar ABACATE, o sistema deve imprimir: 'PARABENS VOCE ACERTOU A FRUTA'
'''

fruta = input('Digite o nome de uma fruta: ')

while fruta.lower() != 'abacate':

# .lower()_ significa que o usario pode digitar maiuscula ou minuscula e o sistema vai reconhecer.
	
	fruta = input('Digite o nome de uma fruta: ')

print('Parabens voce acertou a fruta')


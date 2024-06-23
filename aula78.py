#desafio - IF, ELIF and ELSE - ponto do churrasco

# imagine que voce quer fazer um churrasco e vai usar um termommetro para mensurar o ponto da carne.

# Dados:
# Temperatura - em graus celsius

#fomrula =
# (graus Fahrenheit - 32) * 5/9 (0,5556) = graus celcius

# exemplo: 120 graus Fahrenheit = 48 graus celcius	

#Temperatura da carne:
# até 120ºF (48º) - crua (selada)
# 120ºF até 130ºF (54º) - ao ponto para o mal
# 130ºF até 140ºF (60º) - ao ponto
# 140ºF até 150ºF (65º) - ao ponto para o bem
# 150ºF até 160ºF (71º)- bem passada
# 160ºF até 170ºF (77º)- muito bem passada
# 170ºF até 180ºF (82º) - queimada

temperatura_carne = int(input('Qual a temperatura da carne? '))

if temperatura_carne < 48:
	print('Cozinhar por mais alguns minutos')

elif temperatura_carne in range(48, 53):
	print('Selada')

elif temperatura_carne in range(54, 60):
	print('Ao ponto para o mal')

elif temperatura_carne in range(61, 65):
	print('Ao ponto')

elif temperatura_carne in range(66, 71):
	print('Ao ponto para o bem')

elif temperatura_carne in range(72, 77):
	print('Bem passada')

elif temperatura_carne in range(78, 80):
	print('Muito bem passada')

elif temperatura_carne >= 81:
		print('Queimada')


	

	


	





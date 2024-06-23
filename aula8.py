#operacoes matemáticas
# +, -, *, /, **, %, //, ()

# * = multipicação
# ** = potenciação
# / = divisão
# // = divisão inteira
# % = resto da divisão
# () = precedencia(explicação abaixo)

# A programação de sistema, obdece a precedencia dos operadores matemáticos

#multiplicacão, depois divisão e soma e subtração

#Exemplo:

calculo = 2 + 2 * 3 / 2 
print (calculo)


calculo2 = (2+2) * 3
print(calculo2)

# como na matemática, ele resolve os parenteses primeiro, e depois multiplica, divide, soma e subtrai


# exemplo de divisão inteira:

total_segundos = 3700
horas = total_segundos // 3600
minutos = (total_segundos % 3600) // 60
segundos = total_segundos % 60

print(f"{horas} horas, {minutos} minutos e {segundos} segundos")
# Saída: 1 hora, 1 minuto e 40 segundos

# exemplo de resto da divisão:

numero1 = 10
numero2 = 10
resto = numero1 % numero2
if resto == 0:
		print("O número 1 é divisível pelo número 2")
else:
		print("O número 1 não é divisível pelo número 2")


		'''
precedência refere-se à ordem em que os operadores são avaliados em uma expressão. Essa convenção segue as mesmas regras de precedência usadas na matemática. É fundamental entender essa ordem para garantir que o código produza os resultados esperados.

Aqui está a ordem de precedência dos operadores em Python:

Parêntesis: Expressões dentro de parêntesis são avaliadas primeiro.
Expoentes: Potenciação (usando o operador **) é realizada em seguida.
Multiplicação e Divisão: Essas operações são executadas da esquerda para a direita.
Somas e Subtrações: Também executadas da esquerda para a direita.
Lembre-se de que, quando operadores têm a mesma precedência, eles são avaliados da esquerda para a direita. No entanto, há uma exceção para a exponenciação. Por exemplo:

2 ** 3 ** 2 é equivalente a 2 ** (3 ** 2), resultando em 512.
(2 ** 3) ** 2 é diferente e resulta em 64.
'''

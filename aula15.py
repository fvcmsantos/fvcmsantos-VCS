# For loop (looping) para letras - usado para percorrer uma lista


for letra in 'Google':
  print(letra)

"/////////" # a duas formas funcionam e dao o mesmo resultado

palavra = 'Melancia'
for letra in palavra:
  print(letra)

# o f' é usado para criar uma string com variaveis e o f'{variáveis}'

for letra in palavra:
  print(f'{letra} esta palavra está dentro {palavra}')
 #  Se usar este comando, o python vai indetificar e informar cada  letra que percetence a palavra indicada.
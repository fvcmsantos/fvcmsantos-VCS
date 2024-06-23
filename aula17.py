# for loop nested - usado quando precisamos verificar se algo está dentro de uma lista.
# outer loop - usando quando precisamos verificar se algo está dentro de uma lista (lado de fora)
# inner loop - usando quando precisamos verificar se algo está dentro de uma lista

for numero1 in range(5):
    print('Produto' + str(numero1))
    for numero2 in range(5):
        print(numero1, numero2)
  
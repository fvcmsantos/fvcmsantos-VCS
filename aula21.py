#operador ternario - usado quando precisamos verificar se algo está dentro de uma lista.

#exemplo: se a pessoa for menor que 16 anos, nao pode votar, se maior, pode votar.

idade = 15

#exemplo de código 1: 
#if idade >= 16: 
    #print('voto permitido')
#else:
    #print('voto nao permitido')  


#exemplo de codigo 2:
resultado = 'voto permitido' if idade >= 16 else 'voto nao permitido'
print(resultado)


'desafio - criar uma funcao lambda e falar se o numero digitado é par ou impar.'

'''
def par_impar(numero):
     if numero % 2 == 0: # % = divisvel por x e o resto é 0
      print(f'O número {numero} é par')
     else:
      print(f'O número {numero} é impar')
par_impar(int(input('Digite um número: ')))
'''

#usando a funcao lambda - código mais simples

par_ou_impar = lambda num: 'par' if num % 2 == 0 else 'impar'

print(par_ou_impar(int(input('Digite um número: '))))	

#o que sao lambda = 

''''

> Função anônima: Não precisa de um nome como as funções normais.
> Curta e concisa: Geralmente são escritas em uma linha.
> Usada em locais onde uma função é necessária: Muitas vezes usada para pequenas tarefas ou como argumentos para outras funções.
'''



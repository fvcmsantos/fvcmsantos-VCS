#Criando um programa que calcula a idade de uma pessoa

'''
ano_nascimento = 1972
idade = 2023 - ano_nascimento

print(idade)
'''

ano_nascimento = int(input("em que ano você nasceu? "))
ano_referência = int(input("qual ano você quer calcular a idade: "))
idade = ano_referência - ano_nascimento

print(idade)

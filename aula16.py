# For loop utilizando If and Else - usado quando precisamos verificar se algo está dentro de uma lista.

"Enviar um e-mail com dentalhes da commpra online (máximo 3 tentativa) para os casos de compras confirmadas"

compra_confirmada = True
dados_compra = "compra no valor de R$ 12,50 e entrega confirmada"


for enviar in range(3):

  if compra_confirmada:
    print(dados_compra)
    print("Dados enviados para o e-mail cadastrado da compra")
    break
    # o break serve para sair do loop e encerrar o programa

else: 
    print("falha na compra")
  
  
  

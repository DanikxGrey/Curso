# Atividade 7

valor1 = int(input ("Escolha um valor: ") )

valor2 = int(input ("Escolha outro valor: ") ) 

valor1, valor2 = valor2, valor1

print ("Valor1 e valor2 trocaram o value das variaveis")
print (valor1, valor2)

valor1, valor2 = valor2, valor1

print("Valores revertidos para ordem original")
print(valor1, valor2)
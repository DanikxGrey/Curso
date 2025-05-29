#Numero palindromo é um numero que se lido da esquerda para a direita e da direita para a esquerda é o mesmo, por exemplo 34543

num = (input("Digite um número: "))

if num == num[:: -1]: # Fatiamento (slice), [inicio:fim:passo]
# :: Não colocamos inicio nem fim, entao pegamos toda a string
# -1, ou seja, anda de trás pra frente
    print (f"O numero {num} é um palindromo")

else:
    print (f"O numero {num} não é um palindromo")
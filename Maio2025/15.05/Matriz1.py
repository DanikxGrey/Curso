matriz = [[0] * 4 for _ in range (4) ]
cont = 0
cont1 = 0

matriz [0] [0] = input("Digite o valor da linha 1, coluna 1 ")
matriz [0] [1] = input("Digite o valor da linha 1, coluna 2 ")
matriz [0] [2] = input("Digite o valor da linha 1, coluna 3 ")
matriz [0] [3] = input("Digite o valor da linha 1, coluna 4 ")

# matriz [1] [0] = input("Digite o valor da linha 2, coluna 1 ")
# matriz [1] [1] = input("Digite o valor da linha 2, coluna 2 ")
# matriz [1] [2] = input("Digite o valor da linha 2, coluna 3 ")
# matriz [1] [3] = input("Digite o valor da linha 2, coluna 4 ")

# matriz [2] [0] = input("Digite o valor da linha 3, coluna 1 ")
# matriz [2] [1] = input("Digite o valor da linha 3, coluna 2 ")
# matriz [2] [2] = input("Digite o valor da linha 3, coluna 3 ")
# matriz [2] [3] = input("Digite o valor da linha 3, coluna 4 ")

# matriz [3] [0] = input("Digite o valor da linha 4, coluna 1 ")
# matriz [3] [1] = input("Digite o valor da linha 4, coluna 2 ")
# matriz [3] [2] = input("Digite o valor da linha 4, coluna 3:")
# matriz [3] [3] = input("Digite o valor da linha 4, coluna 4:")

for cont in range (4):
        
        for cont1 in range (4):
            
            print (matriz [cont] [cont1], end="|")
print()
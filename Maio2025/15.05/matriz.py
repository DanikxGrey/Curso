# Inicializa uma lista de listas chamada matriz para representar matriz 4x4
# Cada lista interna representa uma linha de matriz, inicializando com 4 zeros
matriz = [[0] * 4 for _ in range (4)]

# Preenche a linha de indice 0 da matriz:
# Atribui o valor 0 ao elemento na linha 0, coluna 0
matriz[0][0] = 0

# Atribui o valor 1 ao elemento na linha 0, coluna 1
matriz[0][1] = 1

# Atribui o valor 0 ao elemento na linha 0, coluna 2
matriz[0][2] = 0

# Atribui o valor 1 ao elemento na linha 0, coluna 3
matriz[0][3] = 1

print(matriz [0] [1])

# Exibindo os valores da matriz:
#for contador1 in range (4):

#    for contador2 in range (4)
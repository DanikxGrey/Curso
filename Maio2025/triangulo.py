# Solicita ao usuário a basa do triângulo
# O valor é convertido para float pois pode conter casas decimais
base = float(input("digite a base do triângulo (cm): "))

# Solicita ao usuário a altura do triângulo
altura = float(input("digite a altura do triângulo (cm): "))

# calcula a área do triângulo usando a fórmula: área = (base * altura) / 2
area = (base * altura) / 2

# Exibe o resultado da area com a unidade em cm
# o f serve para habilitar a interpolação de variaveis dentro da string entre chaves {}

area = (base * altura) / 2
print(f"A área do triângulo é: ", {area}, "cm²")
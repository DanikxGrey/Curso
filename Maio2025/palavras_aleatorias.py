import random

entrada = input("Digite as palavras separadas por espaço: ").split()

if entrada:
    palavra_aleatoria = random.choice(entrada)
    print(f"A palavra aleatória é: {palavra_aleatoria}")
else:
    print("Nenhuma palavra foi digitada.")
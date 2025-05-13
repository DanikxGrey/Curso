# Iniciamos listas com zeros para de finir o tamanho.
nome = [0] * 2
idade = [0] * 2

# A váriavel 'cont' é usada como índice par percorrer as listas
cont = 0

# Loop 'for' em python que itera de 0 até 2 (inclusive).
for cont in range(3):

    # Imprime o cabeçalho do cadastro, incrementando 'cont' Para exibit o número do cadastro.
    print(f"--- {cont + 1}° Cadastro --- ")
    print()

    # Solicita e lê o nome do usuário, armazenando ele na lista nome na posição 'cont'.
    print("Digite seu nome: ")
    nome[cont] = input()

    # Solicita e lê a idade do usuário, convertendo a entrada para inteiro e armazenando na lista 'idade'
    # É possivel colocar a string diretamente dentro do 'input()' ao invés de usar um print separado como na linha 17
    idade[cont] = (input ("Digite sua idade: ") )
    
    # Solicita e lê o telefone do usuário, armazenandi ele
    # Simula a limpeza de tela
print("\n")

# Outro loop 'for' para exibit os dados cadastrados.
for cont in range (3):
    # Imprime os dados de cada pessoa formatados.
    print(f"nome: {nome [cont] } ")
    print(f"idade: {idade [cont] } anos")
    print("--- --- --- --- --- --- ---")
# Lista para armazenar os nomes cadastrados
cadastros = []

while True:
    print("\n1 - Adicionar nome \n2 - Listar nomes \n3 - Sair")
    # \n serve para dar uma quebra de linha em uma string
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input ("Digite o nome: ") # Pede ao usuario para digitar um nome
        cadastros.append(nome) # Adiciona 'nome' a lista 'cadastros'
        print("Nome cadastrado")

    elif opcao == "2":
        print("\nLista de nomes:")
        for nome in cadastros: # Exibe todos os nomes cadastrados
            print(nome)

    elif opcao == "3":
        print("Saindo do programa...")
        break # finaliza o programa
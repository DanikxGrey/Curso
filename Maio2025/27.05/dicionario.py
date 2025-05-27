# Dicionario para armazenar os alunos e suas idades
# Dicionarios sao definidos por chaves {}
alunos = {}

#Listas de nomes predefinidos
nomes = ["Ana", "Carlos", "Bianca", "Felipe"]

#Pergunta a idade a cada aluno e salva no dicionarios
for nome in nomes:
    idade = input(f"Digite a idade de {nome}") #Entrada de idade
    alunos [nome] = idade #Adiciona ao dicionario
print (alunos)
# Utilize ctrl + : para transformar codigo em comentario e vice versa

alunos = ["rafaela", "Pedro", "Bianca", "Jessica", "Bruno"]


# print (alunos[2])
# print (alunos[3])
# print (alunos)

# for alunos in alunos:
#     print(alunos)


# alunos.append('Helena')
# # Adiciona um elemento ao final da lista.
# print(alunos)


# alunos.insert (3, "Daniela")
# # Insert adiciona uma string a uma posição da variavel
# # Insere um elemento em uma posição específica da lista, deslocando os elementos subsequentes para a direita.
# print (alunos)


# removido = alunos.pop(2)  # Remove o elemento na posição 2 ("Bianca")
# # Remove e retorna o elemento na posição especificada. Se nenhum índice for fornecido, remove o último elemento.
# print(alunos)  # Saída: ['Rafaela', 'Pedro', 'Jessica', 'Bruno']
# print(removido)  # Saída: Bianca
# alunos.pop()  # Remove o último elemento ("Bruno")
# print(alunos)  # Saída: ['Rafaela', 'Pedro', 'Jessica']
# print(removido)


# alunos.remove("Bianca")  # Remove a primeira ocorrência de "Bianca"
# # Remove a primeira ocorrência do elemento especificado na lista. 
# # Levanta um erro ValueError se o elemento não estiver presente.
# print(alunos)  # Saída: ['Rafaela', 'Pedro', 'Jessica', 'Bruno']


# alunos.clear()  # Remove todos os elementos
# # Remove todos os elementos da lista, deixando-a vazia.
# print(alunos)  # Saída: []


# alunos.extend(["Helena", "Daniela"])
# # Adiciona todos os elementos de um iterável (como outra lista) ao final da lista.
# print(alunos)  # Saída: ['Rafaela', 'Pedro', 'Bianca', 'Helena', 'Daniela']


# print(alunos.index("Pedro"))  # Saída: 1
# # Retorna o índice da primeira ocorrência de x na lista. Levanta um ValueError se x não estiver presente. 
# # Pode limitar a busca a um intervalo com start e end.


# print(alunos.index("Pedro"))  # Saída: 1
# # Retorna o número de ocorrências de x na lista

# alunos.sort()
# print(alunos)  # Saída: ['Bianca', 'Pedro', 'Rafaela']
# alunos.sort(reverse=True)
# print(alunos)  # Saída: ['Rafaela', 'Pedro', 'Bianca']
# # Ordena os elementos da lista in-place (modifica a lista original). 
# # Pode usar uma função key para personalizar a ordenação e reverse=True para ordenar em ordem decrescente.


# alunos.reverse()
# print(alunos)  # Saída: ['Bianca', 'Pedro', 'Rafaela']
# # Inverte a ordem dos elementos da lista in-place


# copia = alunos.copy()
# print(copia)  # Saída: ['Rafaela', 'Pedro', 'Bianca']
# copia.append("Helena")
# print(alunos)  # Saída: ['Rafaela', 'Pedro', 'Bianca'] (original não é alterado)
# # Retorna uma cópia rasa (shallow copy) da lista


# # Observações
# # Métodos in-place vs. não in-place: Métodos como .append(), .insert(), .pop(), .remove(), .clear(), .sort() e .reverse() 
# # modificam a lista original (são in-place). Já métodos como .index() e .count() apenas retornam informações sem alterar a lista. 
# # O método .copy() cria uma nova lista.
# # Erros comuns: Métodos como .remove() e .index() levantam um ValueError se o elemento não existir. 
# # Sempre verifique se o elemento está na lista antes de usá-los, se necessário:

# if "Bianca" in alunos:
#    alunos.remove("Bianca")

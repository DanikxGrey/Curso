#Terminar o codigo mais tarde

def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2  # calcula a média
    if media >= 7:
        return "Aprovado"       # devolve "Aprovado"
    else:
        return "Reprovado"      # devolve "Reprovado"
    














    
    
# Claro! Vou explicar com calma e um exemplo prático, assim fica bem claro.

# ---

# ### O que são **parâmetros** em funções e para que servem?

# Parâmetros são **valores que você passa para dentro da função** para ela usar e trabalhar com eles.

# Imagine que uma função é uma **receita de bolo** e os parâmetros são os ingredientes que você escolhe usar naquela receita. Dependendo do ingrediente (parâmetro), o bolo pode ficar diferente.

# Ou seja, parâmetros deixam a função **mais flexível**, porque ela pode fazer coisas diferentes dependendo do que você passar para ela.

# ---

# ### O que é o **`return`** e para que serve?

# O `return` é a palavra usada dentro da função para **devolver um resultado**.

# Quando você usa `return`, a função termina a execução e envia um valor de volta para quem chamou a função.

# Sem `return`, a função pode fazer algo (como imprimir na tela), mas não devolve nada para ser usado depois.

# ---

# ### Exemplo prático

# Vamos criar uma função que calcula a média de duas notas e diz se o aluno passou ou não.

# ```python
# def calcular_media(nota1, nota2):
#     media = (nota1 + nota2) / 2  # calcula a média
#     if media >= 7:
#         return "Aprovado"       # devolve "Aprovado"
#     else:
#         return "Reprovado"      # devolve "Reprovado"
# ```

# Aqui:

# * `nota1` e `nota2` são os **parâmetros** — as notas que você vai passar para a função.
# * A função calcula a média.
# * Depois usa o `return` para **devolver a situação do aluno** ("Aprovado" ou "Reprovado").

# ---

# ### Como usar essa função

# ```python
# resultado = calcular_media(8, 6)
# print(resultado)
# ```

# Saída:

# ```
# Aprovado
# ```

# Se você mudar as notas:

# ```python
# resultado = calcular_media(5, 4)
# print(resultado)
# ```

# Saída:

# ```
# Reprovado
# ```

# ---

# ### Resumo

# * **Parâmetros** são os dados que você dá para a função usar.
# * **`return`** devolve um resultado que você pode guardar numa variável e usar depois.

# Quer tentar criar uma função juntos? Posso ajudar!

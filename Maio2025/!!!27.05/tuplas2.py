#da ao usuário a opção de escolher quais serão as frutas na tupla
print("digite três frutas para a tupla:")
print("1°:")
primeira = input()
print("2°")
segunda = input()
print("3°")
terceira = input()
 
#usa as variaveis criadas para fazer a tupla
frutas =(primeira,segunda,terceira)
#mostra quais vão ser as frutas da tupla 
print("minha tupla de frutas:", frutas)

print ("primeira fruta", frutas[0])
print("segunda fruta:", frutas[1])
print("terceira fruta:", frutas[2])

#usa o comando "len" para informar a quantia de elementos que contem na tupla 
print("numero de frutas na tupla:", len(frutas))
 

print("listando todas as frutas na tupla:")
for fruta in frutas:
    print(fruta)



print("fale uma fruta:")
fruta1 = input()
if fruta1 in frutas:
    print( fruta1, "está na tupla!")

elif fruta1:
    print(fruta1,"não esta na tupla")

#sempre quando criado uma tupla de apenas 1 elemento,
#é necessário a vírgula no final 
unica_fruta = ("melancia",)
print("tupla de um unico elemento:",unica_fruta)
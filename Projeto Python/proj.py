print("Bem vindo ao site!")
nome = input("Digite seu nome aqui: ")

#print("Olá " + nome)
#idade = input("Qual é sua idade?")
#print(nome + ", você têm " + idade + " anos")

#Criar um arquivo#
with open("base_dadis.csv" , "a") as arquivo: 
    arquivo.write(f"Seja bem vindo(a) {nome}.\n")



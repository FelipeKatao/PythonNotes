import os
import Arquivos 
FINALIZAR = "/sair"
Entrada_usuario = ""
Opcoes_usuario = ["0 - Ler anotação"," 1- Escrever anotação"," 2- Lembrar anotacao"]

while Entrada_usuario != FINALIZAR:
    print("=================")
    for a in Opcoes_usuario:
        print(a)
    print("=================")
    Entrada_usuario = input("O que deseja fazer? ")

    if Entrada_usuario == "0":
        Entrada_usuario = input("Qual o nome da sua anotação: ")
        Arquivos.LerArquivos(Entrada_usuario+".txt")

    if Entrada_usuario == "1":
        Entrada_usuario = input("Qual o nome da sua anotação: ")
        Arquivos.CriarArquivo(Entrada_usuario+".txt")
    
    if Entrada_usuario == "2":
        Arquivos.ListarAnotacao()
    os.system("cls")
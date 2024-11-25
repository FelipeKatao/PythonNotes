
import os

def CriarArquivo(NomeDaAnotacao):
    Valores = []
    Entrada_usuario =""
    with open(NomeDaAnotacao,'w',encoding='utf-8') as arquivo:       
        while Entrada_usuario != "/parar":
            Entrada_usuario= input("> ")
            if Entrada_usuario == "/parar":
                break
            Valores.append(Entrada_usuario)

        for b in Valores:
            arquivo.write(b+"\n")

def LerArquivos(NomeDaAnotacao):
    with open(NomeDaAnotacao,'r',encoding='utf-8') as arquivo:
        for d in arquivo:
            print(d)
    input(".")

def ListarAnotacao():
    Arquivos = os.listdir()
    for i in Arquivos:
        if ".txt" in  str(i) :
            print(i)
    input(".")

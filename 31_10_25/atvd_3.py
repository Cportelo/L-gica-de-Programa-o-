import os
os.system("cls")

# Texto que deseja salvar.

Texto = input("digite seu nome :")

# Definir nome do arquivo pra salavar
nome_arquivo = "exemplo.txt" 

# comandos pra salvar.

with open (nome_arquivo, "w") as meu_arquivo:
    meu_arquivo.write(Texto)
    print("Salvo com sucesso !")
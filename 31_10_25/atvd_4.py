import os
from dataclasses import dataclass

os.system("CLS")

@dataclass
class Aluno:
    nome: str
    idade: int
    email: str
    telefone: int 

QUANTIDADE_ALUNOS = 2
lista_alunos= []

print("solicitando dados do aluno.")
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome= input("Digite seu nome: "),
        idade= int(input("Digite sua idade: ")),
        email=input("Digite seu email: ") ,
        telefone= int(input("Digite seu telefone: "))
    )
    lista_alunos.append(aluno)
    
print()
print("Salvando dados.")
arquivo = "dados_aluno.txt"

with open(arquivo, "w") as arquivos_alunos:
    for aluno in lista_alunos:
        arquivos_alunos.write(f"{aluno.nome}, {aluno.idade}, {aluno.email}, {aluno.telefone}\n")
    print("salvo com sucesso !")
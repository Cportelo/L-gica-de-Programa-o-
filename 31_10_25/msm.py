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
lista_alunos = []

print("solicitando dados do aluno.")
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome=input("Digite seu nome: "),
        idade=int(input("Digite sua idade: ")),
        email=input("Digite seu email: "),
        telefone=int(input("Digite seu telefone: "))
    )
    lista_alunos.append(aluno)

print()
print("Salvando dados.")
arquivo = "dados_aluno.txt"

with open(arquivo, "w") as arquivos_alunos:
    for aluno in lista_alunos:
        arquivos_alunos.write(f"Nome: {aluno.nome}\n")
        arquivos_alunos.write(f"Idade: {aluno.idade}\n")
        arquivos_alunos.write(f"Email: {aluno.email}\n")
        arquivos_alunos.write(f"Telefone: {aluno.telefone}\n")
        arquivos_alunos.write("\n")  # Adiciona uma linha em branco entre os alunos

# Definindo o arquivo como somente leitura para evitar edições
os.chmod(arquivo, 0o444)

print("Dados salvos com sucesso!")
print(f"O arquivo {arquivo} foi configurado como somente leitura.")

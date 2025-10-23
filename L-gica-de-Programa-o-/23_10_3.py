import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Pessoa:
    nome: str
    email: str
    endereco: str

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Endereço: {self.endereco}")
        print("-" * 30)

    def mostrar_somente_nome(self):
        print(f"Nome: {self.nome}")
        print("-" * 30)


print("Solicitando os dados da primeira pessoa:")
pessoa1 = Pessoa(
    nome=input("Digite o nome: "),
    email=input("Digite o e-mail: "),
    endereco=input("Digite o endereço: ")
)

print("\nSolicitando os dados da segunda pessoa:")
pessoa2 = Pessoa(
    nome=input("Digite o nome: "),
    email=input("Digite o e-mail: "),
    endereco=input("Digite o endereço: ")
)

print("\n= Exibindo todos os dados =")
pessoa1.mostrar_dados()
pessoa2.mostrar_dados()

print("\n= Exibindo apenas os nomes =")
pessoa1.mostrar_somente_nome()
pessoa2.mostrar_somente_nome()

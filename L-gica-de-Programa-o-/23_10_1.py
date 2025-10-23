import os
from dataclasses import dataclass

os.system("cls") 


@dataclass
class pessoa :
    nome: str
    email: str
    telefone: str
    endereço: str

    def mostrar_dados (self):

        print("=== Exibindo Dados ===")
        print("")
        print(f"Nome: {self.nome}")
        print(f"email: {self.email} ")
        print(f"telefone: {self.telefone} ")
        print(f"endereço: {self.endereço} ")










print("Solicitando os dados da pessoa ")
pessoa1 = pessoa(nome= input("Digite seu nome :"),
                 email=input("Digite seu email:"),
                 telefone=input("Digite seu telefone:"),
                 endereço=input("Digite seu indereço:"))

print("=== Exibindo Dados ===")
print("")
print(f"Nome: {pessoa1.nome}")
print(f"email: {pessoa1.email} ")
print(f"telefone: {pessoa1.telefone} ")
print(f"endereço: {pessoa1.endereço} ")

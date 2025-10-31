import os
from dataclasses import dataclass

os.system("cls")  # limpa a tela (Windows)

# Definindo a classe Endereco
@dataclass
class Endereco:
    logradouro: str
    numero: int

# Definindo a classe Pessoa com Endereco como um atributo
@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float
    endereco: Endereco  # Relacionamento com Endereco

# Solicitando os dados da pessoa
print("Solicitando os dados da pessoa.")
# Criando o objeto corretamente
pessoa1 = Pessoa(
    nome=input("Digite seu nome: "), 
    idade=int(input("Digite sua idade: ")),
    peso=float(input("Digite seu peso: ")),
    altura=float(input("Digite sua altura: ")),
    endereco=Endereco(  # Solicitar dados do endereço
        logradouro=input("Digite o logradouro do seu endereço: "),
        numero=int(input("Digite o número da sua casa: "))
    )
)

# Exibindo os dados
print("\n=== Exibindo Dados ===")
print(f"Nome: {pessoa1.nome}")
print(f"Idade: {pessoa1.idade} anos")
print(f"Peso: {pessoa1.peso} kg")
print(f"Altura: {pessoa1.altura} m")
print(f"Endereço: {pessoa1.endereco.logradouro}, {pessoa1.endereco.numero}")

# Calculando e mostrando o IMC
imc = pessoa1.peso / (pessoa1.altura ** 2)
print(f"IMC: {imc:.2f}")

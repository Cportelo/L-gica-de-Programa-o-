import os
from dataclasses import dataclass

os.system("cls")  # limpa a tela (Windows)

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

("Solicitando os dados da pessoa .")
# Criando o objeto corretamente
pessoa1 = Pessoa(nome=input("Digite seu nome : "), 
                 idade=int(input("Digite sua idade : ")),
                 peso= float(input("Digite seu peso :")),
                 altura=float(input("Digite sua altura: ")))

# Exibindo os dados
print("=== Exibindo Dados ===")
print("")
print(f"Nome: {pessoa1.nome}")
print(f"Idade: {pessoa1.idade} anos")
print(f"Peso: {pessoa1.peso} kg")
print(f"Altura: {pessoa1.altura} m")

# Calculando e mostrando o IMC
imc = pessoa1.peso / (pessoa1.altura ** 2)
print(f"IMC: {imc:.2f}")

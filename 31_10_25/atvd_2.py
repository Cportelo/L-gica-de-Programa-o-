import os
from dataclasses import dataclass

os.system("cls")  # limpa a tela (Windows)

# Classe Autor
@dataclass
class Autor:
    nome: str
    biografia: str

# Classe Livro, com relacionamento para Autor
@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor  # Relacionamento

    # Método para exibir detalhes
    def exibir_detalhes(self):
        print("\n=== Detalhes do Livro ===")
        print(f"Título: {self.titulo}")
        print(f"Ano de publicação: {self.ano}")
        print(f"Autor: {self.autor.nome}")
        print(f"Biografia: {self.autor.biografia}")

# Solicitando os dados do autor
print("=== Cadastro do Autor ===")
autor1 = Autor(
    nome=input("Digite o nome do autor: "),
    biografia=input("Digite a biografia do autor: ")
)

# Solicitando os dados do livro
print("\n=== Cadastro do Livro ===")
livro1 = Livro(
    titulo=input("Digite o título do livro: "),
    ano=int(input("Digite o ano de publicação: ")),
    autor=autor1
)

# Exibindo os detalhes do livro
livro1.exibir_detalhes()

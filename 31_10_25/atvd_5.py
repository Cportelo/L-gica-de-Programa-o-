import os

# Limpa a tela (Windows)
os.system("cls")

# Classe Autor
@dataclass
class Autor:
    nome: str
    biografia: str

# Classe Livro
@dataclass
class Livro:
    nome: str
    autor: Autor
    categoria: str
    preco: float

    # Método para exibir os detalhes
    def exibir_detalhes(self):
        print("\n=== Detalhes do Livro ===")
        print(f"Nome: {self.nome}")
        print(f"Autor: {self.autor.nome}")
        print(f"Categoria: {self.categoria}")
        print(f"Preço: R${self.preco:.2f}")

# Função para salvar dados em um arquivo
def salvar_catalogo(livros, arquivo):
    with open(arquivo, 'w', encoding='utf-8') as f:
        for livro in livros:
            f.write(f"Nome: {livro.nome}\n")
            f.write(f"Autor: {livro.autor.nome}\n")
            f.write(f"Categoria: {livro.categoria}\n")
            f.write(f"Preço: R${livro.preco:.2f}\n")
            f.write("="*20 + "\n")

# Função principal
def cadastrar_livros():
    livros = []
    for i in range(3):  # Para cadastrar 3 livros
        print(f"=== Cadastro do Livro {i + 1} ===")
        nome = input("Digite o nome do livro: ")
        autor_nome = input("Digite o nome do autor: ")
        autor_biografia = input("Digite a biografia do autor: ")
        categoria = input("Digite a categoria do livro: ")
        preco = float(input("Digite o preço do livro: R$"))

        # Criando instância de Autor e Livro
        autor = Autor(nome=autor_nome, biografia=autor_biografia)
        livro = Livro(nome=nome, autor=autor, categoria=categoria, preco=preco)

        # Adicionando livro à lista
        livros.append(livro)

    # Salvando no arquivo
    salvar_catalogo(livros, "catalogo_livros.txt")
    print("\nDados dos livros salvos com sucesso em 'catalogo_livros.txt'!")

# Chamando a função principal
if __name__ == "__main__":
    cadastrar_livros()

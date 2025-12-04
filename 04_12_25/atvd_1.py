import os
import time
from dataclasses import dataclass
from typing import List, Optional

# Limpar terminal
os.system('cls || clear ') 

# --- Estruturas de Dados ---

# Lista principal de clientes e produtos
lista_clientes: List['Cliente'] = []
lista_produtos: List['Produto'] = []

# --- Classes (Cliente e Produto) ---

@dataclass
class Cliente:
    """Representa um cliente com nome, email e telefone."""
    nome: str
    email: str
    telefone: str
    # O atributo 'endereco' do slide não foi incluído para manter 
    # a consistência com o código inicial fornecido.

    def mostrar_dados(self):
        """Método para mostrar as informações dos clientes."""
        print(f'Nome: {self.nome} \nE-mail: {self.email} \nTelefone: {self.telefone}')

@dataclass
class Produto:
    """Representa um produto com nome, quantidade, lote e validade."""
    nome: str
    quantidade: int
    lote: str
    validade: str # Usando str para simplificar, idealmente seria um objeto datetime

    def mostrar_dados(self):
        """Método para mostrar as informações dos produtos."""
        print(f'Nome: {self.nome} \nQuantidade: {self.quantidade} \nLote: {self.lote} \nValidade: {self.validade}')

# --- Funções Auxiliares Comuns ---

def obter_entrada_int(mensagem: str, erro_mensagem: str = 'Entrada inválida. Digite um número inteiro.') -> int:
    """Lê uma entrada do usuário, garantindo que seja um número inteiro."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print(erro_mensagem)
            time.sleep(1)

def limpar_tela_pausar(pausa: int = 2):
    """Pausa a execução e limpa a tela."""
    time.sleep(pausa)
    os.system('cls || clear')


# --- CRUD de CLIENTE ---

def lista_clientes_esta_vazia() -> bool:
    """Verifica se a lista de clientes está vazia e notifica o usuário."""
    if not lista_clientes:
        print('\nNão há clientes cadastrados.')
        return True
    return False

def adicionar_cliente():
    """Adiciona um novo cliente na lista."""
    print('\n ------ Adicionar novo cliente -----')
    nome = input('Digite o nome: ')
    email = input('Digite o E-mail: ')
    telefone = input('Digite o Telefone: ')

    novo_cliente = Cliente(nome=nome, email=email, telefone=telefone)
    lista_clientes.append(novo_cliente)
    print(f'\n Cliente **{nome}** adicionado com sucesso!')

def encontrar_cliente_por_email(email_buscar: str) -> Optional[Cliente]:
    """Encontra um cliente na lista pelo E-mail (busca não sensível a maiúsculas/minúsculas)."""
    email_buscar_lower = email_buscar.lower()
    for cliente in lista_clientes:
        if cliente.email.lower() == email_buscar_lower:
            return cliente
    return None

def mostrar_todos_clientes():
    """Mostra todos os clientes cadastrados."""
    if lista_clientes_esta_vazia():
        return
    
    print('\n---- Lista de Clientes ----')
    for i, cliente in enumerate(lista_clientes, 1):
        print(f'\n--- Cliente {i} ---')
        cliente.mostrar_dados()
    print('--------------------------')

def atualizar_clientes():
    """Atualiza os dados de um cliente existente."""
    if lista_clientes_esta_vazia():
        return
    
    mostrar_todos_clientes()
    print('\n----- Atualizar dados do cliente ----')
    email_buscar = input('Digite o E-mail do cliente para atualizar: ')
    cliente_para_atualizar = encontrar_cliente_por_email(email_buscar)

    if cliente_para_atualizar:
        print('\n--- Cliente Encontrado ---')
        cliente_para_atualizar.mostrar_dados()
        print('\nDigite os novos dados ou deixe **em branco** para manter o valor atual.')
        
        # --- Solicitar novos dados ---
        print(f'E-mail atual: {cliente_para_atualizar.email}')
        novo_email = input('Novo email: ')
        print(f'Nome atual: {cliente_para_atualizar.nome}')
        novo_nome = input('Novo nome: ')
        print(f'Telefone atual: {cliente_para_atualizar.telefone}')
        novo_telefone = input('Novo telefone: ')

        # --- Atualizar dados ---
        if novo_nome:
            cliente_para_atualizar.nome = novo_nome
        if novo_email:
            cliente_para_atualizar.email = novo_email
        if novo_telefone:
            cliente_para_atualizar.telefone = novo_telefone

        print(f'\n Dados do Cliente **{email_buscar}** atualizados com sucesso!')
    else:
        print(f'\n Cliente com E-mail: **{email_buscar}** não encontrado.')

def excluir_cliente():
    """Exclui um cliente da lista."""
    if lista_clientes_esta_vazia():
        return
    
    mostrar_todos_clientes()
    email_buscar = input('\nDigite o E-mail do cliente que deseja excluir: ')
    cliente_para_remover = encontrar_cliente_por_email(email_buscar)

    if cliente_para_remover:
        lista_clientes.remove(cliente_para_remover)
        print(f'\nCliente **{cliente_para_remover.email}** excluído com sucesso!')
    else:
        print(f'\nCliente com o E-mail **{email_buscar}** não encontrado.')

# --- CRUD de PRODUTO ---

def lista_produtos_esta_vazia() -> bool:
    """Verifica se a lista de produtos está vazia e notifica o usuário."""
    if not lista_produtos:
        print('\nNão há produtos cadastrados.')
        return True
    return False

def adicionar_produto():
    """Adiciona um novo produto na lista."""
    print('\n ------ Adicionar novo produto -----')
    nome = input('Digite o nome do produto: ')
    
    # Validação simples para Quantidade (deve ser um inteiro)
    quantidade = obter_entrada_int('Digite a quantidade: ')
    
    lote = input('Digite o lote: ')
    validade = input('Digite a data de validade (Ex: DD/MM/AAAA): ')

    novo_produto = Produto(nome=nome, quantidade=quantidade, lote=lote, validade=validade)
    lista_produtos.append(novo_produto)
    print(f'\n Produto **{nome}** adicionado com sucesso!')

def encontrar_produto_por_nome(nome_buscar: str) -> Optional[Produto]:
    """Encontra o primeiro produto na lista pelo Nome (busca não sensível a maiúsculas/minúsculas)."""
    nome_buscar_lower = nome_buscar.lower()
    for produto in lista_produtos:
        if produto.nome.lower() == nome_buscar_lower:
            return produto
    return None

def mostrar_todos_produtos():
    """Mostra todos os produtos cadastrados."""
    if lista_produtos_esta_vazia():
        return
    
    print('\n---- Lista de Produtos ----')
    for i, produto in enumerate(lista_produtos, 1):
        print(f'\n--- Produto {i} ---')
        produto.mostrar_dados()
    print('--------------------------')

def atualizar_produto():
    """Atualiza os dados de um produto existente."""
    if lista_produtos_esta_vazia():
        return
    
    mostrar_todos_produtos()
    print('\n----- Atualizar dados do produto ----')
    nome_buscar = input('Digite o nome do produto para atualizar: ')
    produto_para_atualizar = encontrar_produto_por_nome(nome_buscar)

    if produto_para_atualizar:
        print('\n--- Produto Encontrado ---')
        produto_para_atualizar.mostrar_dados()
        print('\nDigite os novos dados ou deixe **em branco** para manter o valor atual.')
        
        # --- Solicitar novos dados ---
        print(f'Nome atual: {produto_para_atualizar.nome}')
        novo_nome = input('Novo nome: ')
        
        print(f'Quantidade atual: {produto_para_atualizar.quantidade}')
        nova_quantidade_str = input('Nova quantidade (deixe em branco para manter): ')
        
        print(f'Lote atual: {produto_para_atualizar.lote}')
        novo_lote = input('Novo lote: ')
        
        print(f'Validade atual: {produto_para_atualizar.validade}')
        nova_validade = input('Nova validade: ')

        # --- Atualizar dados ---
        if novo_nome:
            produto_para_atualizar.nome = novo_nome
            
        if nova_quantidade_str:
            try:
                produto_para_atualizar.quantidade = int(nova_quantidade_str)
            except ValueError:
                print('Quantidade inválida, mantendo valor atual.')
                
        if novo_lote:
            produto_para_atualizar.lote = novo_lote
            
        if nova_validade:
            produto_para_atualizar.validade = nova_validade

        print(f'\n Dados do Produto **{nome_buscar}** atualizados com sucesso!')
    else:
        print(f'\n Produto com Nome: **{nome_buscar}** não encontrado.')

def excluir_produto():
    """Exclui um produto da lista."""
    if lista_produtos_esta_vazia():
        return
    
    mostrar_todos_produtos()
    nome_buscar = input('\nDigite o nome do produto que deseja excluir: ')
    produto_para_remover = encontrar_produto_por_nome(nome_buscar)

    if produto_para_remover:
        lista_produtos.remove(produto_para_remover)
        print(f'\nProduto **{produto_para_remover.nome}** excluído com sucesso!')
    else:
        print(f'\nProduto com o nome **{nome_buscar}** não encontrado.')


# --- Menu Principal e Execução ---

def menu_crud(tipo_entidade: str):
    """Exibe o menu CRUD para a entidade selecionada e gerencia as operações."""
    while True:
        print(f"""
---- Gerenciador de {tipo_entidade} ----
1- Adicionar {tipo_entidade[:-1]}
2- Mostrar todos {tipo_entidade}
3- Atualizar {tipo_entidade[:-1]}
4- Excluir {tipo_entidade[:-1]}
9- Voltar ao Menu Principal

""")
        try:
            opcao = obter_entrada_int('Digite uma das opções acima: ')
        except ValueError:
            print('\nEntrada inválida. Digite um número...')
            limpar_tela_pausar()
            continue

        if tipo_entidade == 'Clientes':
            match opcao:
                case 1: adicionar_cliente()
                case 2: mostrar_todos_clientes()
                case 3: atualizar_clientes()
                case 4: excluir_cliente()
                case 9: break
                case _: print('\nOpção inválida \nTente novamente.')
        
        elif tipo_entidade == 'Produtos':
            match opcao:
                case 1: adicionar_produto()
                case 2: mostrar_todos_produtos()
                case 3: atualizar_produto()
                case 4: excluir_produto()
                case 9: break
                case _: print('\nOpção inválida \nTente novamente.')

        if opcao != 1 and opcao != 9:
            limpar_tela_pausar(3)
        elif opcao == 1:
            limpar_tela_pausar(1)
            
        if opcao != 9:
             os.system('cls || clear')


# --- Programa Principal ---

while True:
    print("""

---- Menu Principal do Sistema Mamão com Açúcar ----
1- Gerenciar Clientes
2- Gerenciar Produtos
0- Sair

""")
    try:
        opcao_principal = obter_entrada_int('Selecione uma opção: ')
    except ValueError:
        print('\nEntrada inválida. Digite um número...')
        limpar_tela_pausar()
        continue

    match opcao_principal:
        case 1: 
            limpar_tela_pausar(0)
            menu_crud('Clientes')
        case 2:
            limpar_tela_pausar(0)
            menu_crud('Produtos')
        case 0:
            print('\nSaindo do programa...')
            break
        case _:
            print('\nOpção inválida \nTente novamente.')
            limpar_tela_pausar()
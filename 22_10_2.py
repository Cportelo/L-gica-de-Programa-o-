from dataclasses import dataclass

@dataclass
class pessoa :
    nome: str
    idade : int

#exmplo de uso de classe 
@dataclass
class Pet:
    nome: str
    idade : int


pessoa1 = pessoa("Alice", 30)
pet1 = Pet("totó" , 4)

print(f"Nome: {pessoa1.nome}, idade:{pessoa1.idade}")
print(f"Nome: {pessoa2.nome}, idade:{pessoa2.idade}")
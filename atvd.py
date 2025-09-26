import os
os.system("cls")

# Definindo variávies para contar e somar.
soma = 0
contador = 0

# Inserir uma nota.
while True:
    nota = float(input("Digite uma nota: "))
    contador += 1 # Adiciona mais um ao contador.
    soma += nota # Soma a nota atual ao valor da variável soma.

    continuar = input("Deseja digitar mais um nota? Digite S ou N: ").lower()
    if continuar == "n":
        print("Calculando média...")
        break

# Calculando média.
media = soma / contador

print(f"\nMédia: {media}")
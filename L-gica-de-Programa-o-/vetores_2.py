import os
os.system("cls")  


qntd_negativos = 0
soma_positivos = 0

#
lista_numeros = []

QUANTIDADE_NUMEROS = 5

print(f"\033[32mSolicitando {QUANTIDADE_NUMEROS} números\033[0m")


for i in range(QUANTIDADE_NUMEROS):
    numero = float(input(f"Digite o número {i + 1}: "))
    lista_numeros.append(numero)

    if numero < 0:
        qntd_negativos += 1
    elif numero > 0:
        soma_positivos += numero


print("\nNúmeros digitados:")
for i in lista_numeros:
    print(f"→ {i}")


print(f"\nQuantidade de números negativos: {qntd_negativos}")
print(f"Soma dos números positivos: {soma_positivos:.2f}")

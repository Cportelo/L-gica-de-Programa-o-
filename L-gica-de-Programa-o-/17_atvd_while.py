import os

os.system("cls") 

while True:
    nota = float(input("Digite o valor da sua nota (0 a 10): "))
    
    if 0 <= nota <= 10:
        break  
    print(" Nota inválida. Digite um valor entre 0 e 10.")

print(f" Sua nota foi: {nota}")

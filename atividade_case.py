import os
os. system ("cls")

print("""
Código \t prato \t\t Valor
    1 \t Picanha \t R$ 25,00
    2 \t Lasanha \t R$ 20,00
    3 \t Strogonoff\t R$ 18,00
    4 \t Bife Acebolado\tR$ 15,00
    5 \t Pão com ovo \t R$ 5,00

""")

codigo = int(input("Digite o código do prato desejado: "))


match codigo:
    case 1:
        print ("pincanha")
    case 2:
        print ("lasenha")
    case 3:
        print ("strogonoff")
    case 4:
        print ("bife acebolado")
    case 5:
        print ("pão com ovo")
import os
os.system ("cls")

login_correto = "cr7@gmail.com"
senha_correta = "123456"
tentativas = 0 
max_tentativas = 3 





while True:
    login = input("Digite seu login: ")
    Senha = input("Digite sua senha:")


    if login == login_correto and Senha == senha_correta:
        print("Login efetuado com sucesso!")
        break
    else:
        tentativas  +=1   
        print("Login ou senha incorretos!")
    if tentativas == max_tentativas:
        print("Número máximo de tentativas antigindo. Tente novamnete ou mais tarde.")
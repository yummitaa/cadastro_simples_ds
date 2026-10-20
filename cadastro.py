#Apenas a tela de visualização
nome = ""
idade = ""
usuario = ""
senha = ""

#variaveis para login
login_usuario = ""
login_senha = ""
while True:
    print("==================")
    print("Sistema de Cadastro")
    print("==================")

    print("1 - Cadastrar")
    print("2 - Fazer login")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")
#Funcionalidades
    #Se  o usuario digitar o valor 1,vai ser exebido
    #a açãpo abaixo (opcao == "1") :
    if (opcao == "1"):
        print("=========================")
        print("=====Tela de Cadastro=====")
        print("==========================")
        nome = input("Digite seu nome: ")
        idade = input("Digite sua idade: ")
        usuario = input("Digite seu usuário: ")
        senha = input("Digite sua senha: ")
        print("\n Cadastro realizado!\n")
    #se digitar 2, abre a tela de login
        print("==========================")
    #se digitar 2, abre a tela de login
    elif(opcao == "2"):
        print("========================")
        print("===Tela de Login===")
        print("========================")
        login_usuario = input("Digite o usuario cadastro: ")
        login_senha = input("digite a senha: ")

        #processamento de usuario e senha
        if login_usuario == usuario and login_senha == senha :
            print("\nLogin realizado com sucesso!\n")
            print("bem vindo,", nome)
        else:
            print("Usuário ou senha incorretos")

    #se digitar 3, sai da execução.
    elif(opcao == "3"):
        print("Você está saindo do cadastro, até mais!")
        break
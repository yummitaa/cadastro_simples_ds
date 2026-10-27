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
            while True:
            print("\nLogin realizado com sucesso!\n")
            print("bem vindo,", nome)
            print("1 - Ver os dados cadastrados")
            print("2 - voltar para o menu anterior")

        usuario_opcao = input("\nEscolha uma das opçôes do menu acima: "
    
         if (usuario_opcao == "1"):
            print("\n========================")
            print("===Dados cadastrados===")
            print("========================\n")
            #mostrar nome, idade e usuario
            print("nome de usuário: ", nome)
            print("idade de usuário ", idade)
            print("usuário: ", usuario)
        elif(usuario_opcao == "2"):
            print("\n Você está voltando para o menu anterior")
            break
        else:
            print("\nOpção digitada inválida, use os números do Menu!")
            #estiver correto entra no caso abaixo
    else:
        print("\nUsuário ou senha incorretos\n")

    #se digitar 3, sai da execução.
    elif(opcao == "3"):
        print("Você está saindo do cadastro, até mais!")
        break

#Apenas a tela de visualização
while True:
    print("==================")
    print("Sistea de Cadastro")
    print("==================")

    print("1 - Cadastrar")
    print("2 - Fazer login")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção: "))
#Funcionalidades
    #Se  o usuario digitarno valor 1,vai ser exebido
    #a açãpo abaixo
    if (opcao == 1) :
        print("=========================")
        print("=====Tela de Cadastro=====")
        print("==========================")
    elif(opcao == 2):
        print("========================")
        print("===Tela de Login===")
        print("========================")
    else: 
        print("Você está saindo do cadastro, até mais!")
        break
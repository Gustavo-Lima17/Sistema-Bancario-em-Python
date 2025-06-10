from funcoes  import visualizar_conta, saque, deposito,linha


while (True):
    print("========== BANCO SANTANDER ==========")

    print("Escolha umas das seguintes opções: ")
    print("1 - Visualizar o extrato \n2 - Sacar dinheiro  \n3 - Depositar dinheiro \n4 - Sair")

    opcao = int(input("Digite sua opção: "))

    linha()
    if opcao == 1: 
        visualizar_conta()
        linha()
    elif opcao == 2:  
        saque()
        linha()
    elif opcao == 3: 
        deposito()
        linha()
    elif opcao ==4:
        print("Saindo do sistema....")
        linha()
        break
    else:
        print("Opcao invalida!")
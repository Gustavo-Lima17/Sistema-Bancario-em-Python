from time import sleep

saldo = 500

def menu():
    while(True):
        print("========== BANCO SANTANDER ==========")
        print("Escolha umas das seguintes opções: ")
        print("1 - Visualizar o extrato \n2 - Sacar dinheiro  \n3 - Depositar dinheiro \n4 - Sair\n5 - Criar Usuario")
        
        opcao = int(input("Digite sua opção: "))
        
        print("Caregando...")
        sleep(2)

        if opcao == 1: 
            visualizar_conta()
            linha()
            sleep(5)
        elif opcao == 2:  
            saque()
            linha()
            sleep(5)
        elif opcao == 3: 
            deposito()
            linha()
            sleep(5)        
        elif opcao ==4:
            print("Saindo do sistema....")
            sleep(5)
            linha()
            break
        elif opcao ==5:
            nome = input("Digite seu nome: ")
            nascimento = input("Digite seu dia, mês e ano de nascimento: ")
            cpf = input("CPF: ")
            endereco = input("Logradouro, número, bairro - Cidade/Sigla: ")
            criar_usuario(nome,nascimento,cpf,endereco)
            linha()    
        else:
            print("Opcao invalida!")

def linha():
    print("-"*40)
    
def visualizar_conta():
    global saldo
    print(f'Seu saldo atual: R${saldo}')
    
def saque():
    global saldo
    print("Quanto você deseja sacar? ")
    valor = float(input("Digite o valor: R$"))
    
    if valor > 0:
        if valor <= saldo:
            saldo -= valor
            print("Valor sacado com sucesso")
        else:
            print(f'Impossivel realizado maior que R${saldo}')
    else:
        print("Não é possivel realizar essa operação!")

def deposito():
    global saldo
    print("Digite o valor que deseja depositar: ")
    valor = float(input("R$"))
    
    if valor > 0:
        saldo += valor
        print("Valor depositado com sucesso")
    else:
        print("Valor invalido para depositar!")

usuarios = []

def criar_usuario(nome, nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario["CPF"] == cpf:
            print("Ja existe uma pessoa com esse cpf")
            sleep(1.4)
    usuario = {
        "nome": nome,
        "Nascimento": nascimento,
        "CPF": cpf,
        "Endereço": endereco
    }
    usuarios.append(usuario)
    sleep(1)
    print("Usuario adicionado com sucesso!")

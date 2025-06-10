saldo = 500
saques_realizado = 0
LIMITE_SAQUES = 3
def linha():
    print("-"*40)
    
def visualizar_conta():
    global saldo
    print(f'Seu saldo atual: R${saldo}')
    
def saque():
    global saldo, saques_realizado
    print("Quanto você deseja sacar? ")
    valor = float(input("Digite o valor: R$"))
    
    if saques_realizado >= LIMITE_SAQUES:
        print('Limite de saques atingido')
        return
    
    if valor < saldo and valor > 500:
        if valor >0:
            saldo -= valor
            print("Valor sacado com sucesso")
            saques_realizado += 1
        else:
            print("Impossivel realizado saque menor que zero")
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
        

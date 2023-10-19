import os
import time
import textwrap

def Limpar_tela():
    if os.name == 'posix':  # Linux/Mac
        os.system('clear')
    elif os.name in ('nt', 'dos', 'ce'):  # Windows
        os.system('cls')

def Menu():
    menu = f'''
=================== MENU ===================
||                                        ||
||  [1]-Depositar  | [4]-Novo Usuario     ||
||  [2]-Sacar      | [5]-Nova Conta       ||
||  [3]-Extrato    | [6]-Listar Contas    ||
||                                        ||
||  [0]-Sair                              ||
||                                        ||
============================================
    '''
    print(menu)
    return input("Digite uma opção: ")

def Act_Deposito(Saldo,Extrato):
    deposito = float(input("Quanto de deposito: "))
    if(deposito<0):
        print("Nao é possivel com valores negativos")
    else:
        Saldo+=deposito
        Extrato += f"Depósito:\tR$ {deposito:.2f}\n"
        print("Deposito concluido!")
    return Saldo, Extrato

def Act_Sacar(Saldo,SaldoDiario,Extrato):
    Sacar = float(input("Quanto ira sacar: "))
    if(Sacar>Saldo):
        print("Valor maior do que disponivel")
    elif(Sacar<0):
        print("Nao é possivel sacar valores negativo")
    elif(SaldoDiario==3):
        print("Maximos de saques atingido")
    elif(Saldo<500.0):
        print("O valor maximo de saque é somente R$500.00")
    else:
        Saldo-=Sacar
        Extrato += f"Saque:\tR$ {Sacar:.2f}\n"
        SaldoDiario+=1
        print("Saque efetuado com sucesso!")
    return Saldo, SaldoDiario, Extrato

def Act_Extrato(Saldo,Extrato):
    print("\n================ EXTRATO ================")
    if Extrato == None:
        print("Não foram realizadas movimentações.")
    else:
        print(Extrato)
        print(f"\nSaldo:\t\tR$ {Saldo:.2f}")
    print("==========================================")


def CriarUser(Users):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, Users)

    if usuario:
        print("\n---- Já existe usuário com esse CPF! ----")
        return

    nome = input("Informe o nome completo: ")
    nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço: ")

    Users.append({"Nome": nome, "Nascimento": nascimento, "CPF": cpf, "Endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    
def CadastrarConta(NumeroContas, Users):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, Users)

    if usuario:
        print("\n--- Conta criada com sucesso! ---")
        return {"Agencia":"0001", "Numero da conta": NumeroContas, "Usuario": usuario}

    print("\n----- Usuário não encontrado, fluxo de criação de conta encerrado! -----")

def ListarConta(Contas):
    for conta in Contas:
        linha = f"""\
            Agência:\t0001
            Conta N°:\t{conta['Numero da conta']}
            CPF Titular:\t{conta['Usuario']['Nome']}
        """
        print("=" * 44)
        print(textwrap.dedent(linha))
    input("Digite para continuar: ")


def _main_():
    Saldo = 0
    SaldoDiario = 0

    Extrato = ""
    Users = []
    Contas = []

    while True:
        Limpar_tela()
        escolha = Menu()
        
        if escolha == "1":
            Saldo, Extrato = Act_Deposito(Saldo,Extrato)     
        elif escolha == "2":
            Saldo, SaldoDiario, Extrato = Act_Sacar(Saldo,SaldoDiario,Extrato)
        elif escolha == "3":
            Act_Extrato(Saldo,Extrato)
        elif escolha == "4":
            CriarUser(Users)
        elif escolha == "5":
            NumeroDeContas = len(Contas) + 1
            conta = CadastrarConta(NumeroDeContas, Users)

            if conta:
                Contas.append(conta)

        elif escolha == "6":
            ListarConta(Contas)
        elif escolha=="0":
            break
        else:
            print("OPÇAO INVALIDA!")
            
        time.sleep(3)

_main_()

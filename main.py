from datetime import datetime

LIMIT_TRANSAÇAO = 10
AGENCIA = "0001"
LIMIT_SAQUES = 3
extrato = ''
saldo = 0
numero_de_saques = 0
usuarios =[]
contas = []



def menu():
    menu = """
[d]Depositar
[s]Sacar
[e]Extrato
[nc]Nova conta
[lc]Listar contas
[nu]Novo usuário
[q]Sair

=> """

    return menu


def data_hora_atual():
     return datetime.now().strftime('%d/%m/%y %H:%M:%S')

def create_usuario(usuarios):
     cpf = input("Informe o CPF (somente número):")
     usuario = filter_usuario(cpf,usuarios)

     if usuario:
        print("Já existe usuário com esse CPF!")
        return

     nome = input("Imforme o nome completo:")
     data_nascimento = input("Informe a data de nascimento:")
     endereco = input("Informe o endereço:")

     usuarios.append({"nome":nome , "data_nascimento" : data_nascimento  , "cpf":cpf , "endereco": endereco})

     print("Usuário criado com sucesso")

def filter_usuario(cpf,usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None

def depositar(saldo,deposito,extrato,contador_tran = 0,/):
     
     
     if contador_tran < LIMIT_TRANSAÇAO:
            if deposito > 0:
                saldo += deposito
                extrato += f"Depósito + R$ {deposito} em {data_hora_atual()} \n"    

                contador_tran += 1

                print(f"Saldo atualizado: R$ {saldo}")
            else:
                print("Digite somente valores acima de 0!")    
     else:  
            print('Você atingiu o maximo de depositos diários!')  

     return saldo , extrato  

def create_conta(agencia,numero_conta, usuarios):
     cpf = input('Informe o cpf do usuário: ')
     usuario = filter_usuario(cpf,usuarios)

     if usuario:
          print("Conta criada com sucesso!")
          return{"agencia":agencia , "numero_conta":numero_conta , "usuario" : usuario}     

     print("Usuário não encontrado , fluxo de criação de conta encerrado!")
     return None

def listar_contas(contas):
     for conta in contas:
          linha = f"""
                Agência:{conta['agencia']}
                C/C {conta['numero_conta']}
                Titular: {conta['usuario']['nome']}
            """
          print('='*100)
          print(linha)

     
def Extrato(saldo,extrato):
      
       print("==================Extrato==================")
       print(extrato if extrato else "Nenhuma movimentação realizada.")
       print(f"Saldo atual: R${saldo}")
       print("===========================================")

def sacar(*, saldo, limite, saque, extrato, numero_saques, limite_saques):
    if numero_saques < limite_saques:
        
        while saque > limite:
            saque = float(input("O valor não pode passar de R$ 500! Digite novamente: "))

        if saque > saldo:
            print(f"Não será possível sacar o dinheiro por falta de saldo! | Seu saldo: R$ {saldo}")
        else:
            saldo -= saque
            numero_saques += 1
            extrato += f"Saque: -R$ {saque} em {data_hora_atual()}\n"
            print(f"Saque realizado! Saldo atual: R$ {saldo}")
        
        print(f"Você ainda pode sacar {limite_saques - numero_saques} vez(es).")

    else:
        print("Você atingiu o limite de saques diários.")

    return saldo, extrato, numero_saques  


while True:

    opcao = input(menu())

    if opcao == "d":
        deposito = float(input("Digite o valor que deseja depositar:")) 

        saldo, extrato = depositar(saldo,deposito,extrato)

    elif opcao == "e":
        Extrato(saldo,extrato)

    elif opcao == "s":
        saque = float(input("Qual é o valor desejado de saque: "))

        saldo, extrato, numero_de_saques = sacar(
        saldo=saldo,
        limite=500,
        saque=saque,
        extrato=extrato,
        numero_saques=numero_de_saques,  
        limite_saques=LIMIT_SAQUES
        
    )
        
    elif opcao == "nu":
         create_usuario(usuarios)
        
    elif opcao == "nc":
         numero_conta = len(contas) + 1
         conta = create_conta(AGENCIA , numero_conta , usuarios )

         if conta:
              contas.append(conta)

    elif opcao == "lc":
         listar_contas(contas)
    
    elif opcao == "q":
        break

    else:
        print("Digito invalido!")

            
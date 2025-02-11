menu = """
[d]Depositar
[s]Sacar
[e]Extrato
[q]Sair

=> """


LIMIT_SAQUES = 3
limite = 500
extrato = ''
saldo = 0
contador = 0

while True:

    opcao = input(menu)

    if opcao == "d":
            deposito = float(input("Digite o valor que deseja depositar:")) 
            saldo += deposito
            extrato += f"Depósito + R$ {deposito} \n"
            
            print(f"Saldo atualizado: R$ {saldo}")
    elif opcao == "e":
            print("==========Extrato==========")
            print(extrato if extrato else "Nenhuma movimentação realizada.")
            print(f"Saldo atual: R${saldo}")
            print("===========================")

    elif opcao == "s":
        if contador < LIMIT_SAQUES:

            saque = float(input("Qual é o valor desejado de saque:"))
            while saque > limite:
                saque = float(input("O valor n pode passar de R$ 500!!! | Digite novamente:"))

            if saque > saldo:
                print(f"Não será possível sacar o dinheiro por falta de saldo! | Seu saldo: R$ {saldo}")   
            else:
                saldo -= saque
                contador += 1
                extrato += f"Saque: -R$ {saque}" 
                print(f"Saque realiziado! Saldo atual: R$ {saldo}")
          
            print(f"Você ainda pode sacar {LIMIT_SAQUES-contador} vez(ez)")     
        else:
            print("Você atingiu o limite de saques diários")
    
    elif opcao == "q":
        break

    else:
        print("Digito invalido!")

            
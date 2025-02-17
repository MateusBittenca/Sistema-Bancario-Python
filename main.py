from datetime import datetime

menu = """
[d]Depositar
[s]Sacar
[e]Extrato
[q]Sair

=> """


LIMIT_TRANSAÇAO = 10
LIMIT_SAQUES = 3
extrato = ''
saldo = 0
numero_de_saques = 0

ultimo_dia = 0




def data_hora_atual():
     return datetime.now().strftime('%d/%m/%y %H:%M:%S')
    

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
            numero_saques += 1  # ✅ Atualiza corretamente o número de saques
            extrato += f"Saque: -R$ {saque} em {data_hora_atual()}\n"
            print(f"Saque realizado! Saldo atual: R$ {saldo}")
        
        print(f"Você ainda pode sacar {limite_saques - numero_saques} vez(es).")

    else:
        print("Você atingiu o limite de saques diários.")

    return saldo, extrato, numero_saques  # ✅ Agora retorna numero_saques atualizado




while True:

    opcao = input(menu)

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
        numero_saques=numero_de_saques,  # ✅ Atualiza corretamente
        limite_saques=LIMIT_SAQUES
        
    )

    
    elif opcao == "q":
        break

    else:
        print("Digito invalido!")

            
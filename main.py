from datetime import datetime

menu = """
[d]Depositar
[s]Sacar
[e]Extrato
[q]Sair

=> """


LIMIT_TRANSAÇAO = 10
LIMIT_SAQUES = 3
limite = 500
extrato = ''
saldo = 0
contador = 0
contador_tran = 0
ultimo_dia = 0




def data_hora_atual():
     return datetime.now().strftime('%d/%m/%y %H:%M:%S')

def mudar_dia():
    global contador , contador_tran , ultimo_dia

    dia_atual = datetime.now().day
    if dia_atual != ultimo_dia:
         contador = 0
         contador_tran = 0
         ultimo_dia = dia_atual

def deposito():
     global contador_tran , saldo , extrato
     
     if contador_tran < LIMIT_TRANSAÇAO:
            
            deposito = float(input("Digite o valor que deseja depositar:")) 
            saldo += deposito
            extrato += f"Depósito + R$ {deposito} em {data_hora_atual()} \n"    

            contador_tran += 1

            print(f"Saldo atualizado: R$ {saldo}")
     else:  
            print('Você atingiu o maximo de depositos diários!')  

def Extrato():
       global saldo

       print("==========Extrato==========")
       print(extrato if extrato else "Nenhuma movimentação realizada.")
       print(f"Saldo atual: R${saldo}")
       print("===========================")

def saque():
      global extrato , saldo , contador

      if contador < LIMIT_SAQUES:

            saque = float(input("Qual é o valor desejado de saque:"))
            
            
            while saque > limite:
                saque = float(input("O valor n pode passar de R$ 500!!! | Digite novamente:"))

            if saque > saldo:
                print(f"Não será possível sacar o dinheiro por falta de saldo! | Seu saldo: R$ {saldo}")   
            else:
                saldo -= saque
                contador += 1
                extrato += f"Saque: -R$ {saque} em {data_hora_atual()}\n" 
                print(f"Saque realizado! Saldo atual: R$ {saldo}")
          
            print(f"Você ainda pode sacar {LIMIT_SAQUES-contador} vez(ez)")     
      else:
            print("Você atingiu o limite de saques diários")





while True:
    mudar_dia()

    opcao = input(menu)

    if opcao == "d":
       deposito()  

    elif opcao == "e":
        Extrato()

    elif opcao == "s":
        saque()
    
    elif opcao == "q":
        break

    else:
        print("Digito invalido!")

            
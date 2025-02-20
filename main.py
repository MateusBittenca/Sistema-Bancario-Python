from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, transacao, conta):
        transacao.aplicar(conta)   

    def adicionar_conta(self, conta):
        self.contas.append(conta)     

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero, cliente, agencia='0001'):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero=numero, cliente=cliente)
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return True
        print('Valor inválido')    
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        print('Valor inválido')    
        return False
     
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo + self.limite:
            return super().sacar(valor)
        print('Valor inválido')    
        return False    
    
    def __str__(self):
        return f'Agência: {self.agencia}\nC/C: {self.numero}\nTitular: {self.cliente.nome}'

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append({
            'tipo': transacao.__class__.__name__,
            'valor': transacao.valor,
            'data': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        })

class Transacao(ABC):
    @abstractmethod
    def aplicar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def aplicar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def aplicar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)

# Funções principais
def filtrar_cliente(cpf, clientes):
    return next((cliente for cliente in clientes if cliente.cpf == cpf), None)

def recuperar_conta_cliente(cliente):
    return cliente.contas[0] if cliente.contas else None

def depositar(clientes):
    cpf = input('Digite o CPF: ')
    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        valor = float(input('Digite o valor do depósito: '))
        conta = recuperar_conta_cliente(cliente)
        if conta:
            cliente.realizar_transacao(Deposito(valor), conta)

def sacar(clientes):
    cpf = input('Digite o CPF: ')
    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        valor = float(input('Digite o valor do saque: '))
        conta = recuperar_conta_cliente(cliente)
        if conta:
            cliente.realizar_transacao(Saque(valor), conta)

def exibir_extrato(clientes):
    cpf = input('Digite o CPF: ')
    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        conta = recuperar_conta_cliente(cliente)
        if conta:
            print('\n========== Extrato ==========' )
            if not conta.historico.transacoes:
                print('Sem transações')
            else:
                for t in conta.historico.transacoes:
                    print(f"{t['tipo']}: R$ {t['valor']:.2f} - {t['data']}")
            print(f'Saldo: R$ {conta.saldo:.2f}')
            print("=============================\n")

def criar_conta(numero_conta, clientes, contas):
    cpf = input('Digite o CPF: ')
    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        conta = ContaCorrente.nova_conta(cliente, numero_conta)
        contas.append(conta)
        cliente.contas.append(conta)
        print(f'Conta {conta.numero} criada com sucesso')
    else:
        print('Cliente não encontrado')

def criar_cliente(clientes):
    cpf = input('Digite o CPF: ')
    if filtrar_cliente(cpf, clientes):
        print('Cliente já cadastrado')
        return
    nome = input('Digite o nome: ')
    data_nascimento = input('Digite a data de nascimento: ')
    endereco = input('Digite o endereço: ')
    clientes.append(PessoaFisica(cpf, nome, data_nascimento, endereco))
    print(f'Cliente {nome} criado com sucesso')

def listar_contas(contas):
    for conta in contas:
        print('='*100)
        print(conta)

def menu():
    return """
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q] Sair
=> """

def main():
    clientes = []
    contas = []
    while True:
        opcao = input(menu()).strip().lower()
        if opcao == 'd':
            depositar(clientes)
        elif opcao == 's':
            sacar(clientes)
        elif opcao == 'e':
            exibir_extrato(clientes)
        elif opcao == 'nc':
            criar_conta(len(contas) + 1, clientes, contas)
        elif opcao == 'lc':
            listar_contas(contas)
        elif opcao == 'nu':
            criar_cliente(clientes)
        elif opcao == 'q':
            break
        else:
            print('Opção inválida')

main()

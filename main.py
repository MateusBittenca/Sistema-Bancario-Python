from abc import ABC, abstractmethod,abstractproperty

from datetime import datetime

class Cliente:
    def __init__(self,endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, transacao, conta):
        transacao.aplicar(conta)   

    def adcionar_conta(self, conta):
        self.contas.append(conta)     

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome,data_nascimento,endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self , numero , cliente, agencia = '0001'  ):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = []

    def saldo(self):
        return self.saldo    
    
    @classmethod
    def nova_conta(cls , cliente , numero):
        return cls(cliente,numero)
    
    def sacar (self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f'Saque de R$ {valor:2f}')
            return True
        print('Valor inválido')    
        return False
    

    def depositar(self , valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f'Depósito de R$ {valor:.2f}')
            return True
        print('Valor inválido')    
        return False
    

class ContaCorrente(Conta):

    def __init__(self, numero, cliente,limite = 500 , limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo + self.limite:
            return super().sacar(valor)

        print('Valor inválido')    
        return False    
    
    def __str__(self):
        return f'''
            Agência: {self.agencia}
            C/C: {self.numero}
            Titular: {self.cliente.nome}
        '''

class Historico:
    def __init__(self):
        self.transacoes = []

    @property
    def transacoes(self):
        return self.transacoes

    def adicionar_transacao(self, transacao):
        self.transacoes.append({
            'tipo':transacao.__class__.__name__,
            'valor':transacao.valor,
            'data':datetime.now().strftime( '%d/%m/%Y %H:%M:%s')
        })        

class transacao(ABC):
    @abstractmethod
    def aplicar(self, conta):
        pass

class Deposito(transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self.valor

    def aplicar(self, conta):
      sucesso = conta.depositar(self.valor)
      if sucesso:
          conta.historico.adicionar_transacao(self)

class Saque(transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self.valor

    def aplicar(self, conta):
       sucesso =  conta.sacar(self.valor)

       if sucesso:
           conta.historico.adicionar_transacao(self) 
     




        
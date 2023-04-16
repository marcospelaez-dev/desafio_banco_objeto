from abc import ABC, abstractclassmethod, abstractproperty

class Cliente:
    def __ini__(self, endereco, contas):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registro(conta)

    def adicionar_conta(self, conta):
        self.conta.append(conta)


class Pessoa_Fisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = historico

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._agencia
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @classmethod
    def sacar(cls, saldo, valor):
        saldo = cls.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Não existe saldo suficiente!")

        elif valor > 0:
            cls._saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        
        else:
            print("Valor informado é inválido!")
            return False
        
        return False
    

class Conta_Corrente(Conta):
    def __init__(self, limite, limite_saques, numero, cliente):
        super().__init__(numero, cliente)
        self.limite = 500
        self.limite_saques = 3


class Historico:
    def __init__(self):
        self._transacoes = []


    @property
    def transacoes(self, tipo):
        self.tipo = tipo
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(tipo)

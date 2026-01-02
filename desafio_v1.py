class Conta:

    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []


    def realizar_transacao():
        pass


    def adicionar_conta():
        pass

    
class Historico:
    pass


class ContaCorrente:

    def __init__(self, limite = 500, limite_saques = 3):
        self._limite = limite
        self._limite_saques = limite_saques


class PessoaFisica:
    
    def __init__(self, cpf, nome, data_nascimento):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento


class Transacao:
    pass


class Deposito:
    
    def __init__(self, valor):
        self._valor = valor


class Saque:
    
    def __init__(self, valor):
        self._valor = valor
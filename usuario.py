from conta import Conta

class Usuario:
    def __init__(self, cpf, nome, data_nasc, endereco):
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, n_conta):
        self.contas.append(n_conta)

    def get_nome(self): return self.nome
    def set_nome(self, nome): self.nome = nome
    
    def get_data_nasc(self): return self.data_nasc
    def set_data_nasc(self, data_nasc): self.data_nasc = data_nasc

    def get_cpf(self): return self.cpf
    def set_cpf(self, cpf): self.cpf = cpf

    def get_endereco(self): return self.endereco
    def set_endereco(self, endereco): self.endereco = endereco

    def get_contas(self): return len(self.contas)

from datetime import datetime

class Conta:
    
    MAX_SAQUE_DIA = 3
    MAX_SAQUE_VALOR = 500.0
    
    def __init__(self, agencia, cpf_cliente, n_conta):
        self.agencia = agencia
        self.saldo = 0
        self.cpf_cliente = cpf_cliente
        self.n_conta = n_conta
        self.extrato = []
        self.cont_saque = 0

    def deposito(self, valor_deposito, /):
        if valor_deposito > 0:
            self.saldo += valor_deposito
            data = datetime.now().strftime("%d/%m/%Y %H:%M")
            self.extrato.append((data, "Depósito", valor_deposito))
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inserido inválido.")

    def saque(self, valor):
        if self.cont_saque == self.MAX_SAQUE_DIA:
            print("Máximo de saques realizado para hoje.")
        elif valor > self.MAX_SAQUE_VALOR:
            print("Valor solicitado excede R$500.00")
        elif valor > self.saldo:
            print("Valor solicitado excede o saldo.")
        elif valor > 0:
            self.saldo -= valor
            data = datetime.now().strftime("%d/%m/%Y %H:%M")
            self.extrato.append((data, "Saque", valor))
            print("Saque realizado com sucesso!")
            self.cont_saque += 1
        else:
            print("Valor inserido inválido.")

    def exibir_extrato(self):
        print("=================== EXTRATO ===================\n")
        if self.extrato == []:
            print("Não foram realizadas movimentações.")
        else:
            for i in range(len(self.extrato)):
                print(f"{self.extrato[i][0]} |{self.extrato[i][1]: ^10}| R$ {self.extrato[i][2]:.2f}\n")
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("===============================================")

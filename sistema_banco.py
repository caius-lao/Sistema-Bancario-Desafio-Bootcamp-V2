from usuario import Usuario
from conta import Conta

class Banco:
    
    AGENCIA = "0001"
    
    def __init__(self, saldo = 0):
        self.saldo = saldo
        self.cont_saque = 0
        self.usuarios = [Usuario("18464189845", "Caius", "05-08-1990", "Rua Oito de Dezembro, 321 - Vila Isabel - Rio de Janeiro/RJ")]
        self.contas = [Conta(self.AGENCIA, 18464189845, 1)]
        self.usuarios[0].adicionar_conta(1)

    def cadastrar_usuario(self):
        verifica = False
        cpf = input("Insira o CPF (somente números): ")

        if len(self.usuarios) > 0:
            for i in range(len(self.usuarios)):
                if cpf == self.usuarios[0].get_cpf():
                    verifica = True
            
        if verifica:
            print("CPF já vinculado a um usuário!")
        else:
            nome = input("Insira o nome completo: ")
            data_nasc = input("Insira a data de nascimento (dd-mm-aaaa): ")
            endereco = input("Insira o endereço (logradouro, nº - bairro - cidade/sigla estado): ")
            self.usuarios.append(Usuario(cpf, nome, data_nasc, endereco))
            print("=== Usuário cadastrado com sucesso! ===")

    def cadastrar_conta(self, agencia):
        cpf = input("Digite o CPF do usuário: ")
        verifica = False
        index = 0
        
        for i in range(len(self.usuarios)):
            if cpf == self.usuarios[i].get_cpf():
                verifica = True
                index = i
                n_conta = self.usuarios[i].get_contas() + 1
                break

        if verifica:
            self.contas.append(Conta(self.AGENCIA, cpf, n_conta))
            self.usuarios[index].adicionar_conta(n_conta)
            print("=== Conta criada com sucesso! ===")
            print(f"===    Número da conta: {n_conta}    ===")
        else:
            print("CPF não está vinculado a nenhum usuário!")

    def exibir_contas(self):
        print("============== CONTAS ===============")
        
        for i in range(len(self.contas)):
            print(f"Usuario: {self.contas[i].cpf_cliente} | Nº da conta: {self.contas[i].n_conta}")
            
        print("=====================================")

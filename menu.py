from sistema_banco import Banco
from conta import Conta

class Menu:
    banco = Banco()
    conta = banco.contas[0]
    menu = """
    ============== MENU ==============
    
    [d]  Depósito
    [s]  Saque
    [e]  Extrato
    [nc] Nova Conta
    [lc] Listar contas
    [nu] Novo Usuario
    [q]  Sair

    => """
    
    def main(self):
        while True:
            op = input(self.menu)
            match op:
                case 'd':
                    self.conta.deposito(float(input("Insira o valor para depósito: ")))
                case 's':
                    self.conta.saque(float(input("Insira o valor para saque: ")))
                case 'e':
                    self.conta.exibir_extrato()
                case 'nc':
                    self.banco.cadastrar_conta(self.banco.AGENCIA)
                case 'lc':
                    self.banco.exibir_contas()
                case 'nu':
                    self.banco.cadastrar_usuario()
                case 'q':
                    break
                case _:
                    print("Opção inválida!")

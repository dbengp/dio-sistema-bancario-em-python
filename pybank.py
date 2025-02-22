class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de saque inválido ou Saldo insuficiente.")

    def transferir(self, valor, conta_destino):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            conta_destino.depositar(valor)
            print(f"Transferência de R${valor:.2f} para {conta_destino.titular} efetivadaa com sucesso.")
        else:
            print("Valor de transferência inválido ou Saldo insuficiente.")

    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")


class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, numero_conta, titular, saldo_inicial=0):
        if numero_conta not in self.contas:
            self.contas[numero_conta] = ContaBancaria(numero_conta, titular, saldo_inicial)
            print(f"Conta criada com sucesso para {titular}.")
        else:
            print("Número de conta já existe.")

    def get_conta(self, numero_conta):
        return self.contas.get(numero_conta)

    def listar_contas(self):
        for numero, conta in self.contas.items():
            print(f"Conta: {numero}, Titular: {conta.titular}, Saldo: R${conta.saldo:.2f}")


# Função principal para interação com o usuário
def main():
    banco = Banco()

    while True:
        print("\n--- Sistema Bancário ---")
        print("1. Criar Conta")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Transferir")
        print("5. Verificar Saldo")
        print("6. Listar Contas")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero_conta = input("Número da Conta: ")
            titular = input("Nome do Titular: ")
            saldo_inicial = float(input("Saldo Inicial: "))
            banco.criar_conta(numero_conta, titular, saldo_inicial)

        elif opcao == "2":
            numero_conta = input("Número da Conta: ")
            valor = float(input("Valor do Depósito: "))
            conta = banco.get_conta(numero_conta)
            if conta:
                conta.depositar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "3":
            numero_conta = input("Número da Conta: ")
            valor = float(input("Valor do Saque: "))
            conta = banco.get_conta(numero_conta)
            if conta:
                conta.sacar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "4":
            numero_conta_origem = input("Número da Conta de Origem: ")
            numero_conta_destino = input("Número da Conta de Destino: ")
            valor = float(input("Valor da Transferência: "))
            conta_origem = banco.get_conta(numero_conta_origem)
            conta_destino = banco.get_conta(numero_conta_destino)
            if conta_origem and conta_destino:
                conta_origem.transferir(valor, conta_destino)
            else:
                print("Conta de origem ou destino não encontrada.")

        elif opcao == "5":
            numero_conta = input("Número da Conta: ")
            conta = banco.get_conta(numero_conta)
            if conta:
                conta.verificar_saldo()
            else:
                print("Conta não encontrada.")

        elif opcao == "6":
            banco.listar_contas()

        elif opcao == "7":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

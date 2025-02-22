class ContaBancaria:
    def __init__(self, numero_conta, titular, senha, saldo=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.senha = senha
        self.saldo = saldo
        self.extrato = []
        self.saques_hoje = 0
        self.limite_saques_diario = 3
        self.conta_bloqueada = False
        self.taxa_manutencao = 10.00  # Taxa mensal

    def depositar(self, valor):
        if self.conta_bloqueada:
            print("Conta bloqueada. Operação não permitida.")
            return
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if self.conta_bloqueada:
            print("Conta bloqueada. Operação não permitida.")
            return
        if self.saques_hoje >= self.limite_saques_diario:
            print("Limite diário de saques atingido.")
        elif valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.saques_hoje += 1
            self.extrato.append(f"Saque: -R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def transferir(self, valor, conta_destino):
        if self.conta_bloqueada:
            print("Conta bloqueada. Operação não permitida.")
            return
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            conta_destino.depositar(valor)
            self.extrato.append(f"Transferência para {conta_destino.titular}: -R${valor:.2f}")
            print(f"Transferência de R${valor:.2f} para {conta_destino.titular} realizada com sucesso.")
        else:
            print("Saldo insuficiente ou valor de transferência inválido.")

    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

    def verificar_extrato(self):
        print("\n--- Extrato Bancário ---")
        for movimento in self.extrato:
            print(movimento)
        print(f"Saldo atual: R${self.saldo:.2f}")

    def cobrar_taxa_manutencao(self):
        if self.saldo >= self.taxa_manutencao:
            self.saldo -= self.taxa_manutencao
            self.extrato.append(f"Taxa de manutenção: -R${self.taxa_manutencao:.2f}")
            print(f"Taxa de manutenção de R${self.taxa_manutencao:.2f} cobrada.")
        else:
            print("Saldo insuficiente para cobrar a taxa de manutenção.")

    def bloquear_conta(self):
        self.conta_bloqueada = True
        print("Conta bloqueada.")

    def desbloquear_conta(self):
        self.conta_bloqueada = False
        print("Conta desbloqueada.")

    def alterar_nome_titular(self, novo_nome):
        self.titular = novo_nome
        print(f"Nome do titular alterado para {novo_nome}.")

    def solicitar_emprestimo(self, valor, prazo_meses, taxa_juros):
        if self.conta_bloqueada:
            print("Conta bloqueada. Operação não permitida.")
            return
        juros_total = valor * (taxa_juros / 100) * prazo_meses
        valor_total = valor + juros_total
        parcela = valor_total / prazo_meses
        print(f"Empréstimo de R${valor:.2f} aprovado.")
        print(f"Valor total a pagar: R${valor_total:.2f}")
        print(f"Parcelas: {prazo_meses} x R${parcela:.2f}")
        self.saldo += valor
        self.extrato.append(f"Empréstimo: +R${valor:.2f}")


class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, numero_conta, titular, senha, saldo_inicial=0):
        if numero_conta not in self.contas:
            self.contas[numero_conta] = ContaBancaria(numero_conta, titular, senha, saldo_inicial)
            print(f"Conta criada com sucesso para {titular}.")
        else:
            print("Número de conta já existe.")

    def get_conta(self, numero_conta):
        return self.contas.get(numero_conta)

    def listar_contas(self):
        for numero, conta in self.contas.items():
            print(f"Conta: {numero}, Titular: {conta.titular}, Saldo: R${conta.saldo:.2f}")

    def gerar_relatorio_contas(self):
        print("\n--- Relatório de Contas ---")
        for numero, conta in self.contas.items():
            print(f"Conta: {numero}, Titular: {conta.titular}, Saldo: R${conta.saldo:.2f}")

    def gerar_relatorio_transacoes(self):
        print("\n--- Relatório de Transações ---")
        for numero, conta in self.contas.items():
            print(f"\n--- Extrato da Conta {numero} ---")
            conta.verificar_extrato()


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
        print("6. Verificar Extrato")
        print("7. Cobrar Taxa de Manutenção")
        print("8. Solicitar Empréstimo")
        print("9. Bloquear Conta")
        print("10. Desbloquear Conta")
        print("11. Alterar Nome do Titular")
        print("12. Listar Contas")
        print("13. Gerar Relatório de Contas")
        print("14. Gerar Relatório de Transações")
        print("15. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero_conta = input("Número da Conta: ")
            titular = input("Nome do Titular: ")
            senha = input("Senha: ")
            saldo_inicial = float(input("Saldo Inicial: "))
            banco.criar_conta(numero_conta, titular, senha, saldo_inicial)

        elif opcao == "2":
            numero_conta = input("Número da Conta: ")
            senha = input("Senha: ")
            conta = banco.get_conta(numero_conta)
            if conta and conta.autenticar(senha):
                valor = float(input("Valor do Depósito: "))
                conta.depositar(valor)
            else:
                print("Conta não encontrada ou senha incorreta.")

        elif opcao == "3":
            numero_conta = input("Número da Conta: ")
            senha = input("Senha: ")
            conta = banco.get_conta(numero_conta)
            if conta and conta.autenticar(senha):
                valor = float(input("Valor do Saque: "))
                conta.sacar(valor)
            else:
                print("Conta não encontrada ou senha incorreta.")

        elif opcao == "4":
            numero_conta_origem = input("Número da Conta de Origem: ")
            senha = input("Senha: ")
            conta_origem = banco.get_conta(numero_conta_origem)
            if conta_origem and conta_origem.autenticar(senha):
                numero_conta_destino = input("Número da Conta de Destino: ")
                conta_destino = banco.get_conta(numero_conta_destino)
                if conta_destino:
                    valor = float(input("Valor da Transferência: "))
                    conta_origem.transferir(valor, conta_destino)
                else:
                    print("Conta de destino não encontrada.")
            else:
                print("Conta de origem não encontrada ou senha incorreta.")

        elif opcao == "5":
            numero_conta = input("Número da Conta: ")
            senha = input("Senha: ")
            conta = banco.get_conta(numero_conta)
            if conta and conta.autenticar(senha):
                conta.verificar_saldo()
            else:
                print("Conta não encontrada ou senha incorreta.")

        elif opcao == "6":
            numero_conta = input("Número da Conta: ")
            senha = input("Senha: ")
            conta = banco.get_conta(numero_conta)
            if conta and conta.autenticar(senha):
                conta.verificar_extrato()
            else:
                print("Conta não encontrada ou senha incorreta.")

        elif opcao == "7":
            numero_conta = input("Número da Conta: ")
            senha = input("Senha: ")
            conta = banco.get_conta(numero_conta)
            if conta and conta.autenticar(senha):
                conta.cobrar_taxa_manutencao()
            else:
                print("Conta não encontrada ou senha incorreta.")

        elif opcao == "8":
            numero_conta = input("Número da Conta: ")
            senha = input("Senha: ")
            conta = banco.get_conta(numero_conta)
            if conta and conta.autenticar(senha):
                valor = float(input("Valor do Empréstimo: "))
                prazo = int(input("Prazo (meses): "))
                taxa = float(input("Taxa de Juros (% ao mês): "))
                conta.solicitar_emprestimo(valor, prazo, taxa)
            else:
                print("Conta não encontrada ou senha incorreta.")

        elif opcao == "9":
            numero_conta = input("Número da Conta: ")
            senha = input("Senha: ")
            conta = banco.get_conta(numero_conta)
            if conta and conta.autenticar(senha):
                conta.bloquear_conta()
            else:
                print("Conta não encontrada ou senha incorreta.")

        elif opcao == "10":
            numero_conta = input("Número da Conta: ")
            senha = input("Senha: ")
            conta = banco.get_conta(numero_conta)
            if conta and conta.autenticar(senha):
                conta.desbloquear_conta()
            else:
                print("Conta não encontrada ou senha incorreta.")

        elif opcao == "11":
            numero_conta = input("Número da Conta: ")
            senha = input("Senha: ")
            conta = banco.get_conta(numero_conta)
            if conta and conta.autenticar(senha):
                novo_nome = input("Novo Nome do Titular: ")
                conta.alterar_nome_titular(novo_nome)
            else:
                print("Conta não encontrada ou senha incorreta.")

        elif opcao == "12":
            banco.listar_contas()

        elif opcao == "13":
            banco.gerar_relatorio_contas()

        elif opcao == "14":
            banco.gerar_relatorio_transacoes()

        elif opcao == "15":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

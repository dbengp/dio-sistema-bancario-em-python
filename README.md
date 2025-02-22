# dio-sistema-bancario-em-python
Criando um Sistema Bancário com Python:

Estrutura Básica do Sistema
Criação de Contas: Cada conta terá um número único, nome do titular e saldo.

Depósito: Adicionar dinheiro à conta.

Saque: Retirar dinheiro da conta, verificando se há saldo suficiente.

Transferência: Transferir dinheiro entre contas.

Segurança: Verificar se a conta existe antes de realizar operações.

Extrato Bancário: Registra todas as transações e permite visualizá-las.

Limite de Saque Diário: Limita o número de saques por dia.

Taxa de Manutenção: Cobra uma taxa mensal da conta.

Empréstimos: Permite solicitar empréstimos com juros.

Bloqueio e Desbloqueio de Conta: Permite bloquear ou desbloquear uma conta.

Alteração de Dados do Titular: Permite alterar o nome do titular.

Relatórios Administrativos: Gera relatórios de contas e transações.

Segurança com Senha: Adiciona autenticação por senha para acessar a conta.

Código usando Orinetação a Objetos. Quais benefícios?

Separação de Responsabilidades: 
A classe ContaBancaria gerencia apenas operações relacionadas à conta.
A classe Banco gerencia todas as contas e operações do banco.
A classe SistemaBancario lida com a interação com o usuário.

Encapsulamento:
Atributos como senha e saldo são protegidos e só podem ser acessados por métodos da própria classe.

Reutilização de Código:
Métodos como autenticar e verificar_extrato são reutilizados em várias operações.

Extensibilidade:
Novas funcionalidades podem ser adicionadas facilmente, como investimentos ou notificações.

class ContaBancaria:
    def __init__(self, numero_conta, nome_titular, saldo_inicial=0):
        self.n_conta = numero_conta
        self.nome = nome_titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        try:
            if valor<0:
                valor = valor + "só para dar erro e ir pro except"
            self.saldo += valor
            print(f"Valor depositado com sucesso, saldo atual de {self.nome}: {self.saldo}")
        except:
            print(f"{valor} é um valor invalido")

    def sacar(self, valor):
        try:
            if valor<0:
                valor = valor + "só para dar erro e ir pro except"
            if (self.saldo - valor)<0:
                print(f"Saldo insuficiente, operacao cancelada")
            else: 
                self.saldo -= valor
                print(f"valor sacado com sucesso, saldo atual de {self.nome}: {self.saldo}")
        except:
            print(f"{valor} é um valor invalido")
    
    def ver_saldo(self):
        print(f"Saldo atual de {self.nome}: {self.saldo}")
    
conta1 = ContaBancaria("123-4", "Joao", 1500.00)
conta2 = ContaBancaria("567-8", "Maria")

conta2.depositar(500)
conta1.sacar(200)
conta2.sacar(1000)
conta1.ver_saldo()
conta2.ver_saldo()
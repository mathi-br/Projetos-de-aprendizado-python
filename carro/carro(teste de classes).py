class Carro:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ligado = False
        self.velocidade = 0
    
    def __repr__(self):
        return f"{self.marca} {self.modelo} {self.cor}, veiculo ligado? {self.ligado}, velocidade: {self.velocidade}"

    def ligar(self):
        if self.ligado==False:
            self.ligado = True
            print("O carro ligado com sucesso")
        else:
            print("O carro já está ligado")
    
    def desligar(self):
        if self.ligado==True and self.velocidade==0:
            self.ligado = False
            print("O carro desligado com sucesso")
        else:
            print("O carro já está desligado//carro precisa estar parado")

    def acelerar(self, valor):
        if self.ligado==True:
            self.velocidade += valor
            print(f"velocidade atual: {self.velocidade}")
        else:
            print(f"Carro desligado, ligue o carro para acelerar")

    def frear(self, valor):
        if (self.velocidade-valor)>0:
            self.velocidade -= valor
            print(f"veiculo reduziu de velocidade, velocidade atual: {self.velocidade}")
        else:
            self.velocidade = 0
            print(f"veiculo freio totalmente, velocidade atual: {self.velocidade}")

carro1 = Carro("wolkesvagem", "fusca", "azul")
print(carro1)
carro1.acelerar(100)
carro1.ligar()
carro1.acelerar(20)
carro1.acelerar(30)
carro1.frear(10)
carro1.desligar()
carro1.frear(50)
carro1.desligar()
print(carro1)
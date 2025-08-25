import random as rd

class Dado():
    def __init__(self):
        self.numero = None #numero atual do dado
        self.conta_faces = [0, 0, 0, 0, 0, 0] #contagem de quantas vezes caiu cada lado
        self.duplo_seis = 0 #contagem de quantos duplo seis cairam

    def __add__(self, other): #para somar o .numero de cada dado
        return self.numero + other.numero
    
    def __repr__(self): #para mostrar oque cada objeto tem/é
        return f"contagem de faces [vezes que caiu 1, vezes que caiu 2.....]{self.conta_faces}, contagem de duplos 6: {self.duplo_seis}"
        
    def rolar(self): #faz a rolagem, salva o numero atual e atualiza a contagem
        self.numero = rd.randint(1,6)
        match self.numero:
            case 1:
                self.conta_faces[0] += 1
            case 2:
                self.conta_faces[1] += 1
            case 3:
                self.conta_faces[2] += 1
            case 4:
                self.conta_faces[3] += 1
            case 5:
                self.conta_faces[4] += 1
            case 6:
                self.conta_faces[5] += 1
        
    def dupla_rolagem(self, other): #faz uma rolagem dupla, com dois objetos dado, checa se teve um duplo 6 e atualiza a contagem do mesmo
        self.rolar()
        other.rolar()
        if self.numero + other.numero == 12:
            self.duplo_seis += 1
            other.duplo_seis += 1
            print("seis duplo!!!")
        
## aqui crio 2 objetos dados para conseguir fazer a rolagem dupla
dado1 = Dado()
dado2 = Dado()

if __name__ == "__main__": #programa principal
    ## aqui crio 2 objetos dados para conseguir fazer a rolagem dupla
    dado1 = Dado()
    dado2 = Dado()

    #aqui mostro que os objetos estão vazios
    print(dado1)
    print(dado2)

    #realizo as rolagens duplas
    for i in range(100): 
        dado1.dupla_rolagem(dado2) #primeiro dado(não importa a ordem dos dados).dupla_rolagem(segundo dado)

    #e mostro como os dados ficaram, com a contagem de rolagens duplas
    print(dado1)
    print(dado2)
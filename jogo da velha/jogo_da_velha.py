## Jogo da velha em Python
## Criar/reiniciar a lista
def listanova():
    lista = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"], ]
    return lista

## mostrar a lista
def mostrarlista(lista):
    linha = 0
    print("    0    1    2  < X")
    for i in lista:
        print(linha, i)
        linha += 1
    print("^\nY\n")

## checar vitoria
def checarvitoria(lista):
    i = ["O", "X"]
    for jogadores in i:
        for linha in lista:
            if (linha[0] == jogadores) and (linha[1] == jogadores) and (linha[2] == jogadores):
                print(f"------------------\njogador: {jogadores}, ganhou\n------------------")
                mostrarlista(lista)
                return False
        for v1 in range(3):
            if (lista[0][v1] == jogadores) and (lista[1][v1] == jogadores) and (lista[2][v1] == jogadores):
                print(f"------------------\njogador: {jogadores}, ganhou\n------------------")
                mostrarlista(lista)
                return False
        if (lista[0][0] == jogadores) and (lista[1][1] == jogadores) and (lista[2][2] == jogadores):
            print(f"------------------\njogador: {jogadores}, ganhou\n------------------")
            mostrarlista(lista)
            return False
        elif (lista[0][2] == jogadores) and (lista[1][1] == jogadores) and (lista[2][0] == jogadores):
            print(f"------------------\njogador: {jogadores}, ganhou\n------------------")
            mostrarlista(lista)
            return False
    return True

## Mudar valores e checar vitorias
def alteracoes(list):
    jogador = ["O", "X"]
    posicoes = ("0", "1", "2")
    for i in jogador:
        while True:
            mostrarlista(list)
            print("-------------------------------------------------------------------------")
            y = input(f"jogador {i}, escolha a posicao em que quer jogar nesta ordem(Y/X): \ny= ")
            x = input("x= ")
            while (not x in posicoes) or (not y in posicoes):
                print("------------------------------------------")
                mostrarlista(list)
                y = input(f"posicoes invalidas, (Y/X): \ny= ")
                x = input("x= ")
            y, x = int(y), int(x)
            if list[y][x]=="-":
                list[y][x] = i
                aux = checarvitoria(list)
                if aux==False:
                    return list, aux
                break
            elif list[y][x]=="O" or list[y][x]=="X":
                v2 = 0
                for linha in list:
                    for coluna in linha:
                        if coluna != "-":
                            v2 += 1
                if v2 == 9 and aux==True:
                    aux = False
                    mostrarlista(list)
                    print("-------------\njogo empatado\n-------------")
                    return list, aux
                else:
                    print("----------------\nposicao invalida\n----------------")
        if not aux == True:
            break
    return list, aux

## programa principal
aux = True
while True:
    lista = listanova()
    while aux:
        lista, aux = alteracoes(lista)
    v1 = (input("deseja jogar novamente? (digite sim para jogar denovo)\n")).lower().strip()
    if not v1=="sim":
        break

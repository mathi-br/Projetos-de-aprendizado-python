## bibliotecas que utilizei
import pandas as pd
import matplotlib.pyplot as plt

## pegando e ajustando os dados e separando nas variaveis
dados = pd.read_csv("dadoscovid/SESRS - Coronavírus_v1.csv")[:-1]
dados = dados.drop(columns=["Unnamed: 0"])

## dados gerais, legenda: 0 = total, 1 = antigos, 2 = novos
totalcasos = [int(dados[" Confirmados "].sum() + dados[" Novos Confirmados "].sum()), int(dados[" Confirmados "].sum()), int(dados[" Novos Confirmados "].sum())]
totalobitos = [int(dados[" Óbitos "].sum() + dados[" Novos Óbitos "].sum()), int(dados[" Óbitos "].sum()), int(dados[" Novos Óbitos "].sum())]
cidademaiscaso = dados.loc[dados[" Novos Confirmados "].idxmax()]
cidademenosmortal = dados.loc[dados[" Mortalidade /100 mil hab  "].idxmin()]
medianovosobitos = round((dados[" Novos Óbitos "].sum())/(len(dados[" Novos Óbitos "])), 3)

## funcao para pegar valores numericos/1 = nao pergunta se quiser continuar
def pegarnumero(v1, v3=1):     
    while True:
            v2 = input(f"-----------------------------------------------------\n{v1}").strip()
            if v2.isdigit():
                v2 = int(v2)
                if v3==0:
                    return v2
                elif v2<=10 and v2>0:
                    return v2
                else:
                    print("-----------------------------------------------------\ninvalido")
            elif v3==0:
                v4 = input("-----------------------------------------------------\nvalor invalido, deseja continuar? (1=sim, qualquer outra coisa = não): ").strip()
                if v4 != "1":
                    return 0
            else:
                print("-----------------------------------------------------\ninvalido")

## dados para o grafico das cidades com mais incidencia
def graficomaisincidente(dados=dados):
    aux1, v1 = {}, "digite o numero de cidades que quer ver, ordem da mais incidente para menos, apenas até 10 cidades: "
    aux = dados.nlargest(pegarnumero(v1), " Incidência /100 mil hab ")
    cidadesmaisincidentes = []
    for chave, valor in aux.to_dict().items():
        if chave==" Incidência /100 mil hab " or chave==" Município ":
            for index, valoremsi in valor.items():
                if not index in aux1:
                    aux1[index] = []
                aux1[index].append(valoremsi)
    for i in aux1:
        cidadesmaisincidentes.append(aux1[i])
    aux, aux1 = [], []
    for i in cidadesmaisincidentes:
        aux.append(i[0].strip())
        aux1.append(i[1])
    cidadesmaisincidentes = [aux, aux1]
    aux, aux1 = [0], 0
    while aux1<max(cidadesmaisincidentes[1]):
        aux1 += 500
        aux.append(aux1)
    eixoy = aux
    plt.bar(cidadesmaisincidentes[0], cidadesmaisincidentes[1])
    plt.yticks(eixoy)
    plt.title("grafico das cidades com maior incidencia de casos de COVID-19")
    plt.ylabel("incidencia por 100mil habitantes")
    plt.grid(axis="y", linestyle="dotted")
    plt.show()

## funcoes para mostrar os dados de forma mais bonitas
def cidades(v1=cidademaiscaso, v2=cidademenosmortal):
    dicii = {}
    while True:
        decisao = input("----------------------------------------------\n1 = cidade com mais casos, 2 = cidade com menor mortalidade: ").strip()
        if decisao == "1":
            v3 = v1
            aux1 = ["com mais casos novos:", "total de casos: "]
            break
        elif decisao == "2":
            v3 = v2
            aux1 = ["com menor nivel de mortalidade:", "Nivel de mortalidade: "]
            break
        else:
            d1 = input("valor invalido, deseja tentar novamente? (1 = sim): ").strip()
            if d1 != "1":
                return "----------------------------------------------\nopcao cancelada pelo usuario"
    for chave, valor in v3.to_dict().items():
        dicii[chave] = valor
    if decisao == "1":
        aux2 = dicii[" Novos Confirmados "]
    else:
        aux2 = dicii[" Mortalidade /100 mil hab  "]
    print(f"Municipio {aux1[0]} {dicii[" Município "]}")
    print(f"{aux1[1]} {aux2}")

## Programa principal
while True:
    v1, v2 = "escolha opcao: ", {1, 2, 3, 4, 5}
    print("---------------------------------------------\nDados referentes ao estado do RS\n---------------------------------------------")
    print("1) numero total de casos confirmados de covid-19\n2) numero total de obitos")
    print("3) dados sobre cidades\n4) media de novos obitos\n5) grafico das cidades com mais incidencias")
    decisao = pegarnumero(v1, 0)
    if not decisao in v2:
        break
    elif decisao == 1:
        print(f"numero de casos confirmados totais: {totalcasos[0]}\ncasos antigos: {totalcasos[1]}\ncaso novos: {totalcasos[2]}")
    elif decisao == 2:
        print(f"numero de obitos confirmados totais: {totalobitos[0]}\nobitos antigos: {totalobitos[1]}\nnovos obitos: {totalobitos[2]}")
    elif decisao == 3:
        cidades()
    elif decisao == 4:
        print(f"a media de novos obitos entre as cidades do RS: {medianovosobitos}")
    elif decisao == 5:
        graficomaisincidente()
    vv1 = input("---------------------------------------------\n1 = continuar (digite qualquer outra coisa para parar): ")
    if vv1!="1":
        break
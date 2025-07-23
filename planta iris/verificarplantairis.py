## bibliotecas que utilizei
import pandas as pd
import matplotlib.pyplot as mt
import numpy as np

## pegando os dados necessarios e criando a amostra de 30%
dataframe = pd.read_csv("planta iris\iris.csv")
dataframe = (dataframe.sample(frac=0.3)).sort_index()

## criando o arquivo da amostra de 30%
with open("planta iris/45iris.txt", "w") as txt:
    dataframe.to_csv(txt, index= False, sep= ",", lineterminator="\n")

## pegando os dados que irao serem utilizados no programa e graficos
distribuicao = round((dataframe["variety"].value_counts(normalize=True))*100, 2)
dados = {}
dadospgrafico = {}
for j in set(dataframe["variety"]):
    dadospgrafico[j] = dataframe.loc[dataframe["variety"] == j].values
for i in dataframe:
    if not i == "variety":
        max1, min1, mean, std = float(dataframe[i].max()), float(dataframe[i].min()), float(dataframe[i].mean()), float(dataframe[i].std()) 
        dados[i]= {"maximo": max1, "minimo": min1, "media": round(mean, 2), "desvio": round(std, 2)}
    elif i == "variety":
        maisfrequente = [(dataframe["variety"].value_counts()).idxmax(), int((dataframe["variety"].value_counts()).max())]

## mostrar grafico
def mostrargraficos(dataset=dadospgrafico):
    
    ## criando listas e conjuntos bases da def
    z2, z1 = {"1", "2"}, {"1", "2", "3"}
    x, y = [], []

    ## pegando os dados
    print("----------------------------------------\nescolha os itens do grafico")
    v1=input("1 = Setosa, 2 = versicolor, 3 = virginica: ")
    v2=input("1 = Sepal, 2 = Petal: ")
    while not(v1 in z1) or not(v2 in z2):
        print("opcao invalida, escolha novamente")
        v1=input("1 = Setosa, 2 = versicolor, 3 = virginica: ")
        v2=input("1 = Sepal, 2 = Petal: ")

    ## ajeitando os valores para criar menos variaveis
    if v1=="1":  v1 = "Setosa"
    elif v1=="2": v1 = "Versicolor"
    elif v1=="3": v1 = "Virginica"
    if v2=="1": v2, v3, v4 = 0, 1, "Sepal"
    elif v2=="2": v2, v3, v4 = 2, 3, "Petal"
    for item in dataset[v1]:
        x.append(item[v2])
        y.append(item[v3])
    xyajeitados = sorted(zip(x, y))
    x, y = zip(*xyajeitados)
    xaj = np.arange(len(x))
    yy = []
    for i in range(0, 5):
        yy.append(i)
        yy.append(i+0.5)
    
    ## criando o grafico
    mt.bar(xaj, y, linewidth=0.4, edgecolor="black", align="center")
    mt.xticks(xaj, x)
    mt.yticks(yy)
    
    ## ajustando e personalizando o grafico
    mt.grid(axis="y", linestyle="dotted", alpha=0.6)
    mt.xlabel(dataframe.columns[v2])
    mt.ylabel(dataframe.columns[v3])
    mt.title(f"grafico: {v1}, sobre: {v4}")
    mt.tight_layout()
    mt.show()

## parar loop do codigo principal
def pararloop():
    x = input("----------------------------------------\ndeseja continuar? (1 para sim)\n")
    if x == "1":
        return True
    else:
        return False

## mostrar as estatisticas gerais de cada campo
def mostraresta(v1=dados):
    print("----------------------------------------")
    for colunas in dados:
        print(f"--------------------\n{colunas}: ")
        for itens in dados[colunas]:
            print(f"{itens} = {dados[colunas][itens]}")

## mostar a destribuicao de uma forma mais bonita
def mostrardistri(v1=distribuicao):
    for chave, valor in distribuicao.to_dict().items():
        print(f"{chave}: {valor}%")

## codigo principal
while True:
    print(f"------------------MENU------------------\n1) distribuicao de amostras por classe")
    print("2) classe com maior numero de amostras\n3) ver opcoes de grafico")
    print("4) ver estatisticas gerais de cada campo numerico\n----------------------------------------")
    opcao = input()
    if opcao == "1":
        print(f"----------------------------------------\ndestribuicao:")
        mostrardistri()
    elif opcao == "2":
        print(f"----------------------------------------\nclasse com mais plantas: ", maisfrequente[0]," com ", maisfrequente[1], "exemplares")
    elif opcao == "3":
        mostrargraficos()
    elif opcao == "4":
        mostraresta()
    else: 
        print("----------------------------------------\nopcao invalida")
    auxi = pararloop()
    if auxi==False:
        break
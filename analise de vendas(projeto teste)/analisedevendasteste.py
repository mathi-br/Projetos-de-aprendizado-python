## bibliotecas que utilizei
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

## carregando dados
dados = pd.read_csv("analise de vendas(projeto teste)/vendas_extenso.csv")
dadosfaltantes = dados.loc[dados[dados.isnull().any(axis=1)].index]
dados = dados.drop(dados[dados.isnull().any(axis=1)].index)

## corrigir e processador dados faltantes
if not dadosfaltantes.empty:
    print("------------------------------------------------------------\ndataset com dados faltantando nos seguintes index:\n------------------------------------------------------------")
    print(dadosfaltantes)
    print("------------------------------------------------------------")
    print("oque deseja fazer sobre estes dados?\n1)trocar dados faltantes para (faltante) \n#)ignora estas linhas")
    aux = input("OBSERVACAO: caso a DATA e VALOR faltar, a linha sera desconsiderada independente da escolha\nqualquer digito diferente de 1 ignora as linhas: ")
    if aux=="1":
        for index, linha in dadosfaltantes.iterrows():
            if pd.isnull(linha["Data"]) or pd.isnull(linha["Valor"]):
                continue
            else:
                for coluna in ["Vendedor", "Produto"]:
                    if pd.isnull(linha[coluna]):
                        dadosfaltantes.loc[index, coluna] = "faltante"
                dados.loc[index] = dadosfaltantes.loc[index]
        dados = dados.sort_index().reset_index()
    else:
        dados = dados.sort_index().reset_index()

## sei que assim é pior mas gosto de escrever assim
def pegadados(v1=dados):
    return v1

## pega numeros \ v1 = texto para pegar numero / v2 = (0=opcoes para o menu)(1=numero float)(2=porcentagem) \ v3 = maior opcao numerica
def peganumeros(v1="", v2=0, v3=10):
    if v2==1 or v2==2:
        while True:
            try:
                aux = round(float(input(v1)),2)
                if v2==1:
                    return aux
                elif v2==2 and (aux<=100 and aux>=0):
                    return aux
                else:
                    print(f"{aux:.2f} é uma porcentagem invalida, porfavor tente novamente")
            except:
                print("Valor invalido, porfavor tente novamente")
    else:
        while True:
            try:
                aux = int(input(v1))
                if aux>=0 and aux<=v3:
                    return aux
                else:
                    print("opcao invalida, porfavor tente novamente")
            except:
                print("Valor invalido, porfavor tente novamente")

## mostrar estrutura e estatisticas basicas sobre os dados
def infobasicas():
    dados = pegadados()
    print("------------------------------\nEstrutura básica\n------------------------------") 
    dados.info()
    print("------------------------------\nEstatisticas iniciais\n------------------------------\n", round(dados.describe(), 2), "\n------------------------------")

## mostra o valor total em vendas
def totalvendas():
    dados = pegadados()
    print("------------------------------\nTotal valor total em vendas:")
    print("R$:",dados["Valor"].sum(),"\n------------------------------")
    
## mostra o total de vendas por vendedor
def vendasvendedor():
    dados = pegadados()
    aux = round(dados.groupby("Vendedor")["Valor"].sum().sort_values(ascending=False), 2)
    print("------------------------------\nTotal de vendas por vendedor:")
    for v1, v2 in aux.to_dict().items():
        print(f"{v1}\t:R$ {v2}")
    print("------------------------------")

## mostra qual é o produto mais vendido
def maisvendido():
    dados = pegadados()
    print("------------------------------\nTabelas itens mais vendidos:")
    print("Produto\t\tQuantidade")
    aux, aux1 = dados["Produto"].value_counts().sort_values(ascending=False), []
    for i in aux.to_dict().keys():
        aux1.append(len(i))
    aux1 = max(aux1)
    for v1, v2 in aux.to_dict().items():
        print(f"{v1:<{aux1}}\t{v2}")
    print("------------------------------")

## mostra as vendas com Valor acima de um valor determinado pelo usuario
def vendasxvalor():
    dados = pegadados()
    print("------------------------------\nVerificador de vendas por determinado valor")
    aux = "---\nOBS: use . e não , / valido apenas 2 numeros decimais, caso colocar\nDigite o valor minimo das vendas: "
    aux = peganumeros(aux, 1)
    aux1 = dados.loc[dados["Valor"]>=aux]
    if len(aux1)>25:
        print(f"------\n{len(aux1)} vendas cujo valor excede R${aux:.2f}")
    elif len(aux1)>0:
        print(f"------\nVendas cujo valor excede R${aux:.2f}: \n{aux1}")
    else:
        print(f"------\nNenhuma venda com valor R${aux:.2f} ou mais")
    print("------------------------------")

## Cria uma dataframe com o valor total vendido pelos vendedores, comissao(personalizada) dos vendedores
def comissaovendedor():
    print("------------------------------\nGerador de dataframe de comissao")
    dados = pegadados()
    aux = (round(dados.groupby("Vendedor")["Valor"].sum(), 2)).reset_index()
    aux1 = "---\ndigite a porcentagem de comissão aos vendedores: "
    aux1 = peganumeros(aux1, 2)
    aux["Comissao"] = round((aux["Valor"]/100)*aux1, 2)
    aux.to_csv("Comissao.csv", index=False)
    print("---\narquivo (Comissao.csv) foi gerado")
    print("------------------------------")

## Criar graficos de vendas por vendedor ou geral
#### eu iria colocar mais opcoes de graficos mas o projeto nao especificou quais graficos eu deveria criar, entao decidi poupar tempo
def criargrafico():
    print("------------------------------\nGraficos por vendedor")
    dados = pegadados()
    aux = "---\nescolha o vendedor para criar o grafico\n(Ana=0)(Beatriz=1)(Carlos=2)(Julia=3)(Lucas=4)(Marina=5) OU (Geral=6): "
    op1 = peganumeros(aux,0,6)
    aux = "---\nescolha qual grafico deseja ver\n(produtos mais caros vendidos=0)(produtos mais vendidos=1): "
    op2 = peganumeros(aux,0,1)
    print("------------------------------")
    aux = list(set(dados["Vendedor"]))
    aux.sort()
    aux.append("Geral")
    aux = aux[op1]

    ## grafico especifico por vendedor
    if op1!=6:
        if op2==0: 
            aux1 = ((dados.groupby("Vendedor")["Valor"].nlargest(7))[aux]).reset_index()
            aux1 = dados.loc[aux1["index"]]
            aux1 = [aux1["Produto"].to_list(), aux1["Valor"].to_list()]
            op1 = "valores mais altos vendidos(R$ arredondado)"
            aux = [aux, "produtos mais caros vendidos", " vendedor(a)"]
        else:
            aux1 = (dados.groupby("Vendedor")["Produto"].value_counts()[aux]).reset_index()
            aux1 = [aux1["Produto"].to_list(), aux1["count"].to_list()]
            op1 = "quantidade vendida"
            aux = [aux, "produtos mais vendidos", " vendedor(a)"]

    ## grafico geral
    else:
        if op2==0: 
            aux1 = ((dados["Valor"].nlargest(7))).reset_index()
            aux1 = dados.loc[aux1["index"]]
            aux1 = [aux1["Produto"].to_list(), aux1["Valor"].to_list()]
            op1 = "valores mais altos vendidos(R$ arredondado)"
            aux = [aux, "produtos mais caros vendidos", ""]
        else:
            aux1 = (dados["Produto"].value_counts()).reset_index()
            aux1 = [aux1["Produto"].to_list(), aux1["count"].to_list()]
            op1 = "quantidade vendida"
            aux = [aux, "produtos mais vendidos", ""]

    ## criando e configurando o grafico
    if aux1[1][0]%1!=0:
        aux1.append([])
        aux1[2] = list(range(len(aux1[0])))
        op2 = [int(min(aux1[1])),int(max(aux1[1]))]
        op2 = [((int(min(op2))//500)*500), ((int(max(op2))//500)*500)]
        op2 = list(range(0, op2[1]+1, 500))
        op2.append(max(aux1[1]))
        aux2 = np.array(op2)
        plt.bar(aux1[2], aux1[1])
        plt.yticks(aux2)
        plt.xticks(aux1[2], aux1[0])
          
    else:
        op2 = [(v1-(min(aux1[1]))+1) for v1 in aux1[1]]
        plt.bar(aux1[0], op2)
        plt.yticks((list(range(min(op2), max(op2)+1))), (list(range(min(aux1[1]), max(aux1[1])+1))))
    
    plt.grid(axis="y", linestyle="dotted", alpha=0.6)
    plt.title(f"Tabela{aux[2]}: {aux[0]}\nsobre {aux[1]}")
    plt.xlabel("--------------------\nProdutos")
    plt.ylabel(f"{op1}\n--------------------")
    plt.show()

## mostrar as linhas com dados faltando
def mostrardadosfaltando():
    print(f"------------------------------\nSituacao dos dados faltantes:")
    if not dadosfaltantes.empty:
        print(dadosfaltantes)
    else:
        print(f"não há dados faltantes")
    print("------------------------------")

## Programa principal
while True:
    print(f"---programa de Analise de vendas (teste)---\nPorfavor selecione uma opcão para ver:")
    aux = "------\n(informacoes básicas=0)\n(total de vendas=1)\n(total de vendas por vendedor=2)\n(produtos mais vendidos=3)\n(vendas acima de valor especifico=4)\n(gerar comissao para vendedor=5)\n(gerar graficos=6)\n(dados faltandos=7)\n(PARAR PROGRAMA=8)\n"
    aux = peganumeros(aux, 0, 8)
    match aux:
        case 0:
            infobasicas()
        case 1:
            totalvendas()
        case 2:
            vendasvendedor()
        case 3:
            maisvendido()
        case 4:
            vendasxvalor()
        case 5:
            comissaovendedor()
        case 6:
            criargrafico()
        case 7:
            mostrardadosfaltando()
        case 8:
            print("------------------------------")
            break
    aux = input("deseja continuar? (sim=1)(se nao digitar nada ou outra coisa o programa sera encerrado): ")
    if not aux=="1":
        print("------------------------------")
        break
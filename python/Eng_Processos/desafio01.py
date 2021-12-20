

import pandas as pd
import os, sys


# Coleta nome e extensão do excel
def coleta_excel(cond=False):
    while cond==False:
        #nome = input("Digite o nome do excel: ")
        #extensao = input("Digite a extensão (exemplo: .xls, .ods): ")
        try:
            #caminho = os.path.join(os.path.abspath('.'),(nome+extensao))
            #print(caminho)
            #df = pd.read_excel(str(caminho))
            df = pd.read_excel(os.path.join(os.path.abspath('.'),"planilha.xls"))
            cond = True
        except:
            print("Problemas com o nome ou com a extensão!")
            coleta_excel()
    return df


# Calcula a dispersão e envia para avalia_decisao
def calcula_dispersao(df):
    # Q, 1-Q, R, 1-R
    R = ((df["Vol. Rel. Adj."].min())/(df["Vol. Rel. Adj."].max()))
    Q = ((df["Vazão"].min())/(df["Vazão"].max()))
    vetor = [Q, 1-Q, R, 1-R]
    avalia_decisao(df, vetor)


def busca_volatilidade(df, coluna, indice):
    return df[coluna][indice]


def busca_indice_maximo(vetor):
    return vetor.index(max(vetor))


# Avalia a decisão do corte
def avalia_decisao(df, vetor):
    coluna_vazao = "Vazão"
    coluna_volatilidade = "Vol. Rel. Adj."
    
    aux = []
    aux.append(min(vetor[1], vetor[2]))
    aux.append(min(vetor[0], vetor[2]))
    aux.append(min(vetor[0], vetor[3]))
    
    indice = busca_indice_maximo(aux)
    
    print(indice)
    # print(vetor)
    # print(aux)
    # sys.exit()

    if indice == 0:
        linha = df.index[df[coluna_vazao] == df[coluna_vazao].max()]
        linhaSuperior = linha-1 if linha != 0 else 0
        # Ver qual das volatilidades é maior --> chama função busca_volatilidade
        vol_maxima = ([busca_volatilidade(df, coluna_volatilidade, linha),
        busca_volatilidade(df, coluna_volatilidade, linhaSuperior)
        ])
        # Fazer o corte

    elif indice == 1:
        n_linhas = len(df.index)

        # Ver se é par
        if n_linhas % 2 == 0:
            # Sem problemas, divide no meio
            pass
        else:
            # Descobre menor relatividade
            pass
        

        
    elif indice == 2:
        # Busca o índice referente maior volatilidade
        linha = df.index[df[coluna_volatilidade] == df[coluna_volatilidade].max()]
        # Realiza o corte

    return aux


def main():
    # 1. Le excel
    # python3 opicional1.py
    df = coleta_excel()
    # 2. Trata dados
    calcula_dispersao(df)
    
    # 3. Fornece fluxograma
    pass


if __name__ == '__main__':
    main()


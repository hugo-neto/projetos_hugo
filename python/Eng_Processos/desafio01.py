# https://www.delftstack.com/pt/howto/python-pandas/slice-columns-in-pandas-dataframe/#:~:text=3%200.377612%200.310408-,Utilize%20redindex()%20para%20fatiar%20colunas%20em%20Pandas%20DataFrame,para%20o%20corte%20de%20colunas.


import pandas as pd
import numpy as np
import os, sys
global cortesDf
cortesDf = []


# Coleta nome e extensão do excel
def coleta_excel(cond=False):
    while cond==False:
        #nome = input("Digite o nome do excel: ")
        #extensao = input("Digite a extensão (exemplo: .xls, .ods): ")
        try:
            #caminho = os.path.join(os.path.abspath('.'),(nome+extensao))
            #print(caminho)
            #df = pd.read_excel(str(caminho))
            #print(os.path.abspath('.'))
            df = pd.read_excel(os.path.join(os.path.abspath('.'),"Dados.xls"))
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


# Busca o valor de colatilidade
def busca_volatilidade(df, coluna, indice):
    return df[coluna][indice]


def limpa_vetor(df):
    try:
        if df in cortesDf:
            cortesDf.remove(df)
    except:
        i = 0
        for item in cortesDf:
            if item.equals(df) == True:
                del cortesDf[i]
            i = i + 1


# Corta o df de acordo com o interesse
def corta_df(df, indice):
    # Abre, lê, e completa arquivo.txt
    arquivo = open('resultado_HugoNeto.txt', 'r')
    conteudo = arquivo.readlines()
    texto = '\t['

    try:
        df1 = df.iloc[0:(indice)+1, :]
        df1["Vol. Rel. Adj."][len(df1)-1] = np.nan
        df2 = df.iloc[indice+1:, :]
        texto = texto + ''.join(str(componente) for componente in df1.iloc[:,0])
        texto = texto + '/' + ''.join(str(componente) for componente in df2.iloc[:,0])
    
    except TypeError:
        df1 = metade(df, 0)
        df2 = metade(df, 1)
        texto = texto + df1['Comp.']
        texto = texto + '/' + df2['Comp.']
    
    texto = texto + ']\n'
    conteudo.append(texto)
    arquivo = open("resultado_HugoNeto.txt", 'w')
    arquivo.writelines(conteudo)
    arquivo.close()
    # Finalizou abertura e leitura dos arquivos de texto

    # Faz a reindexação se a variável for do tipo dataframe
    # Quando chega em 2 componentes, ele acaba gerando uma Series ao invés de DataFrame
    if isinstance(df1, pd.DataFrame) and isinstance(df2, pd.DataFrame):
        if df1.index.start != 0:
            df1.reset_index(inplace=True, drop=True)
        if df2.index.start != 0:
            df2.reset_index(inplace=True, drop=True)

    cortesDf.append(df1)
    cortesDf.append(df2)

    limpa_vetor(df)


# Avalia a decisão do corte
def avalia_decisao(df, vetor):
    coluna_vazao, coluna_volatilidade = "Vazão", "Vol. Rel. Adj."

    # Reseta o index para começar do zero    
    df.reset_index(inplace=True, drop=True)

    aux = []
    aux.append(min(vetor[1], vetor[2]))
    aux.append(min(vetor[0], vetor[2]))
    aux.append(min(vetor[0], vetor[3]))
    
    # Busca índice referente ao valor máximo para aplicar regras herísticos
    indice = aux.index(max(aux))

    # Regra V1a
    if indice == 0:
        linha = list(df.index[df[coluna_vazao] == df[coluna_vazao].max()])[0]
        if len(df) == 4:
            print(linha)

        if linha == 0:
            return corta_df(df, linha)

        if busca_volatilidade(df, coluna_volatilidade, linha) > busca_volatilidade(df, coluna_volatilidade, linha-1):
                # corte realizado no meio e resto
            return corta_df(df, linha)
        else:
        # corte realizado meio-1
            return corta_df(df, linha-1)

    # Regra V1b
    elif indice == 1:
        n_linhas = len(df.index)

        # Ver se é par
        if n_linhas % 2 == 0:
            # Sem problemas, divide no meio
            linhas = len(df)/2
            return corta_df(df, linhas)
        else:
            # Descobre menor relatividade
            # Pivo do meio da lista
            cont = int(len(df)/2)
            if busca_volatilidade(df, coluna_volatilidade, cont) > busca_volatilidade(df, coluna_volatilidade, cont-1):
                # corte realizado no meio e resto
                return corta_df(df, cont)
            else:
                # corte realizado meio-1
                return corta_df(df, cont-1)
    
    # Regra V2
    elif indice == 2:
        # Busca o índice referente maior volatilidade (formato estranho) + converte em lista + int em seguida
        linha = list(df.index[df[coluna_volatilidade] == df[coluna_volatilidade].max()])[0]
        # Realiza o corte
        return corta_df(df, linha)


def inicia_cortes(df):
    calcula_dispersao(df)
  

def metade(df, indice):
    limpa_vetor(df)
    df1 = df.iloc[indice, :]
    return df1


def main():
    # 1. Le excel
    # python3 opicional1.py
    df = coleta_excel()
    cortesDf.append(df)
    # 2. Trata dados
    # Cria txt
    resultado = open("resultado_HugoNeto.txt", "a")
    # Abre ele com permissões de escrita
    resultado = open("resultado_HugoNeto.txt", "w")
    # Declara string que disserta sobre o problema
    texto = """
    Método heurístico, assistido por lógica nebulosa
    Objetivo: sínteses de um sistema de separação
    Apenas colunas de destilação
"""
    # escreve no arquivo
    resultado.write(texto)
    # Após escrever, fecha
    resultado.close()
    contador = len(df)
    
    while len(cortesDf) < contador:
        for item in cortesDf:
            if len(item) > 1 and isinstance(item, pd.DataFrame):
                inicia_cortes(item)
    print("Programa executado com sucesso")


if __name__ == '__main__':
    print("Iniciando programa")
    main()

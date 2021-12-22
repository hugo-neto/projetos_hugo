# https://www.delftstack.com/pt/howto/python-pandas/slice-columns-in-pandas-dataframe/#:~:text=3%200.377612%200.310408-,Utilize%20redindex()%20para%20fatiar%20colunas%20em%20Pandas%20DataFrame,para%20o%20corte%20de%20colunas.


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


# Corta o df de acordo com o interesse
def corta_df(df, indice):
    # Corta até o índice
    vetor_f = []
    df1 = df.iloc[0:(indice)+1, :]
    df2 = df.iloc[indice:, :]
    vetor_f.append(df1)
    vetor_f.append(df2)
    return vetor_f


def abre_txt(nome="resultado_HugoNeto.txt"):
    return open(nome, "w")


# Avalia a decisão do corte
def avalia_decisao(df, vetor):
    coluna_vazao = "Vazão"
    coluna_volatilidade = "Vol. Rel. Adj."
    
    aux = []
    aux.append(min(vetor[1], vetor[2]))
    aux.append(min(vetor[0], vetor[2]))
    aux.append(min(vetor[0], vetor[3]))
    
    # Busca índice referente ao valor máximo para aplicar regras herísticos
    indice = aux.index(max(aux))

    # Regra V1a
    if indice == 0:
        linha = list(df.index[df[coluna_vazao] == df[coluna_vazao].max()])[0]

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
    vetor_final = calcula_dispersao(df)
    
    arquivo = abre_txt()
    texto = '['
    texto = texto + ''.join(str(componente) for componente in vetor_final[0].iloc[:,0])
    texto = texto + '/' + ''.join(str(componente) for componente in vetor_final[1].iloc[:,0])
    texto = texto + ']'
    arquivo.write(texto)

    # Ver questão de dois cortes por etapa!
    for item in vetor_final:
        if type(item) == list and len(item) > 2:
            vetor = inicia_cortes(item)
    pass


# A função main já cria o txt na pasta
def main():
    # 1. Le excel
    # python3 opicional1.py
    df = coleta_excel()

    # 2. Trata dados
    # Cria txt
    resultado = open("resultado_HugoNeto.txt", "a")
    # Abre ele com permissões de escrita
    resultado = abre_txt()
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

    inicia_cortes(df)
    


if __name__ == '__main__':
    main()

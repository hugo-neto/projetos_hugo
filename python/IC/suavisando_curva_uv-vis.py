# Fonte: https://stackoverflow.com/questions/20618804/how-to-smooth-a-curve-in-the-right-way


import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter


def main():
    # uv_vis:
    # 1 = Análise pilha
    # 2 = Análise GO método Hummers
    for i in range(0,3):
        df = pd.read_csv('uv_vis'+str(i+1)+'.csv', delimiter="\t")
        df = df.abs()
        #df = df.loc[df['Absorbancia'] >= 0.1]
        df = df.iloc[83:, 0:2]
        #83
        # df = df.iloc[0:n, 0:2].abs()
        # df = df.iloc[0:n, 0:2].abs()
        # o 51 não sei o pq mas o n°2 é o grau da função
        yhat = savgol_filter(df['Absorbancia'], 51, 2)
        #df['Absorbancia']
        plt.plot(df['nm'], yhat)
        plt.ylabel('Absorbância')
        plt.xlabel('Comprimento de Onda [nm]')
        plt.title('Análise de UV/Vis - Solução Óxido de Grafeno')
        #plt.xticks(range(219, 870))
        plt.show()  
        a = input("Digite qualquer tecla para próximo: ")


if __name__ == '__main__':
    main()


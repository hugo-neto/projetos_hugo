# Fonte: https://stackoverflow.com/questions/20618804/how-to-smooth-a-curve-in-the-right-way


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter


# Realiza a anotação do ponto máximo
def annot_max(x,y, ax=None):
    xmax = x[np.argmax(y)]
    ymax = y.max()
    text= "Comp. Onda={:.3f}, Absorbância={:.3f}".format(xmax, ymax)
    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60")
    kw = dict(xycoords='data',textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
    ax.annotate(text, xy=(xmax, ymax), xytext=(0.7,0.9), **kw)
    #, xytext=(0.94,0.96), **kw


def main():
    # uv_vis:
    # 1 = Análise pilha
    # 2 = Análise GO método Hummers
    for i in range(0,3):
        fig, ax = plt.subplots()
        df = pd.read_csv('uv_vis'+str(i+1)+'.csv', delimiter="\t")
        df = df.abs()
        #df = df.loc[df['Absorbancia'] >= 0.1]
        df = df.iloc[83:, 0:2]
        #83

        yhat = savgol_filter(df['Absorbancia'], 51, 2)

        #df['Absorbancia']

        ax.plot(df['nm'],yhat)

        plt.ylabel('Absorbância')
        plt.xlabel('Comprimento de Onda (nm)')
        plt.title('Análise de UV/Vis - Solução Óxido de Grafeno')
        
        annot_max(np.array(df['nm']),np.array(yhat))
        
        plt.ylim(0, 0.7)
        plt.show()  
        a = input("Digite qualquer tecla para próximo: ")


if __name__ == '__main__':
    main()


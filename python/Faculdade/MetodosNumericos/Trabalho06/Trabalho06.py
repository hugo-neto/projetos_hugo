
from mpl_toolkits.axes_grid1 import host_subplot
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt


# Vetores para armazenar valores que serão plotados no gráfico
x1_v, x2_v, h_v = [], [], []


def f1(x1, x2, F):
    total = ((0.53)*(x1)*(x2))/(0.12 + x2) - ((F/10) + 0.01)*x1
    return total


def f2(x1, x2, F):
    total = (F/10)*(4-x2) - (2.5)*((0.53*x1*x2)/(0.12 + x2))
    return total


def plota_grafico(x1_v, x2_v, h_v):
    host = host_subplot(111)

    par = host.twinx()

    host.set_xlabel("Tempo (h)")
    host.set_ylabel("Concentração Células [Kg/m³]")
    par.set_ylabel("Concentração Substrato [Kg/m³]")

    p1, = host.plot(h_v, x1_v, label="Concentração Células")
    p2, = par.plot(h_v, x2_v, label="Concentração Substrato")

    leg = plt.legend()

    host.yaxis.get_label().set_color(p1.get_color())
    leg.texts[0].set_color(p1.get_color())
    par.yaxis.get_label().set_color(p2.get_color())
    leg.texts[1].set_color(p2.get_color())

    plt.show()


def plota_grafico_unico(xi_v, h_v, texto="Concentração da espécie", condicao=True):
    fig, ax = plt.subplots()

    # Using plot(..., dashes=...) to set the dashing when creating a line
    if condicao == True:
        line2, = ax.plot(h_v, xi_v,'-r', label=texto)
    else:
        line2, = ax.plot(h_v, xi_v, label=texto)
    
    #Linha referente à legenda no canto do gráfico
    ax.legend()
    #Mostrar/Plotar o gráfico
    plt.show()


def main():
    condicao = True
    while condicao == True:
        print("\nCaso deseje parar o loop, digite '0'")
        F = float(input("Digite a vazão F em [m³/h]: "))
        print("")
        if F == 0:
            break
        
        h = 0.1
        # u = u do presente momento
        ua1, ua2 = 1.65, 0.2

        h_v.append(0.0), x1_v.append(ua1), x2_v.append(ua2)

        while h <= 30.1:
            # hp = passo
            hp = 0.1

            # gij; i = índice g; j = Céluas (1) ou Substrato (2)
            g11 = hp*f1(ua1, ua2, F)

            aux = 0.5*g11 + ua1
            g21 = hp*f1(aux, ua2, F)

            aux = 0.5*g21 + ua1
            g31 = hp*f1(aux, ua2, F)

            aux = ua1 + g31      
            g41 = hp*f1(aux, ua2, F)
            # ua = u antes
            u1 = ua1 + (1/6)*(g11 + 2*g21 + 2*g31 + g41)

        # ---------------------------------------------------------------------- #

            g12 = hp*f2(ua1, ua2, F)

            aux = 0.5*g12 + ua2
            g22 = hp*f2(ua1, aux, F)

            aux = 0.5*g22 + ua2
            g32 = hp*f2(ua1, aux, F)

            aux = ua2 + g32
            g42 = hp*f2(ua1, aux, F)
            u2 = ua2 + (1/6)*(g12 + 2*g22 + 2*g32 + g42)

            x1_v.append(u1)
            x2_v.append(u2)
            h_v.append(h)

            h = h + 0.1
            ua1, ua2 = u1, u2

        plota_grafico(x1_v, x2_v, h_v)
        plota_grafico_unico(x1_v, h_v, "Concentração Células")
        plota_grafico_unico(x2_v, h_v, "Concentração Subtrato", False)


if __name__=='__main__':
    main()

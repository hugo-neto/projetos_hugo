#https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/line_demo_dash_control.html#sphx-glr-gallery-lines-bars-and-markers-line-demo-dash-control-py

import numpy as np
import matplotlib.pyplot as plt


def plota_grafico():
    #[a,b (intervalo a,b) ,nº de subdivisões]
    x = np.linspace(-1, 1, 10000)
    #f(x) = cos(x)
    #f(x) pode ser seno!
    #y = np.sin(x)
    y = np.cos(x)
    
    r = (313*x**4 - 6900*x**2 + 15120)/(13*x**4 + 660*x**2 + 15120)

    fig, ax = plt.subplots()

    # Using set_dashes() to modify dashing of an existing line
    
    #line1, = ax.plot(x, r, label='r(x) Padé')
    line1.set_dashes([2, 6, 2, 6])  # 2pt line, 2pt break, 10pt line, 2pt break

    # Using plot(..., dashes=...) to set the dashing when creating a line
    line2, = ax.plot(x, y , dashes=[4, 6], label='cos(x)')

    line3 = ax.plot(x, (y-r), dashes=[3,3], label='|f(x) - r(x)|')

    #Linha referente à legenda no canto do gráfico
    ax.legend()
    #Mostrar/Plotar o gráfico
    plt.show()


def principal():
    plota_grafico()


if __name__=='__main__':
    principal()

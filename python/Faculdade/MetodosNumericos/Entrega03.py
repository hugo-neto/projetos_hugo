# Hugo de Lacerda Coutinho Neto
# DRE: 118060251
# 15/10/2020


import numpy as np
import matplotlib.pyplot as plt
from math import exp

epslon, delta2, kmax = 10**-6, 10**-7, 100


def f(x):
    termo = x + 0.1 - (0.05*exp((20*x)/(1 + x)))/(1 + 0.1*exp((20*x)/(1 + x)))
    a = (20*x)/(1 + x)
    return termo


def wegstein(a, b):
    fa, fb = f(a), f(b)
    ai, bi = a, b

    if fa*fb > 0:
        print("Entre com novos valores de a e b:")
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))

    y, delta1, k = 1, 1, 0
    while (delta1 > epslon or abs(y) > delta2) and k < kmax:
        multiplicador = fa/(fa - fb)
        x0 = a + multiplicador*(b - a)
        y = f(x0)
        
        if y*fa > 0:
            fa = y
            a = x0
        else:
            fb = y
            b = x0
        delta1 = abs(b-a)
        k = k + 1

    if k < 100:
        print("Raiz encontrada!")
        print(f"Para o intervalo [{ai},{bi}] com {k} interações termos:")
        print(f"| x0 = {x0} | f(x0) = {f(x0)} |")
    else:
        print("Não fora possível identificar as raízes para o intervalo indicado.")

def grafico():
    aux = -0.5
    fig, ax = plt.subplots()
    
    # xt -> x TOTAL
    # ft -> f(xt)    
    eixox, eixoy, xt, ft = [], [], [], []

    for i in range(0,151):     
        aux = aux + 0.01                
        if aux == -1:
            continue
        
        eixox.append(aux)
        eixoy.append(0)

        try:
            ft.append(f(aux))
            xt.append(aux)            
        except OverflowError:
            pass        
        
    x1 = np.array(xt)
    fx = np.array(ft)

    primeiros_pontos, = ax.plot(x1, fx, label='f(x) CSTR')
    # primeiros_pontos.set_dashes([2, 2, 10, 2])
    eixo_cartesiano, = ax.plot(eixox, eixoy)

    ax.legend()    
    plt.show()  


def main():     
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    wegstein(a, b)
    grafico()

if __name__=='__main__':
    main()


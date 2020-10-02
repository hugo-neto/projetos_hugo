# Criador: Hugo de Lacerda Coutinho Neto
# Métodos Numéricos
# DRE: 118060251
# 02/10/2020

import numpy as np
import matplotlib.pyplot as plt

x, aux = np.linspace(0, 10, 500), -1

y = [-0.4, 0.4, 0.5, 0.4]
x = [-0.5, 0.5, 1, 2]
x_user, y_user, p = [-1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 2.51], [], []


def printa_user(x_user, y_user):
    print("Abaixo mostramos alguns valores de x e f(x) calculados")
    for i in range(0,len(x_user)):        
        print(f"x{i} {x_user[i]} = {y_user[i]}")


def limpa_interpoladores(p):
    p.clear()


def gera_y_user(x_user):
    for i in range(0,len(x_user)):
        aux = interpoladores_lagrange(x_user[i], x, y, p)
        y_user.append(aux)
    return y_user


def interpoladores_lagrange(xe, x, y, p):
    for i in range(0,4):
        p.append(1)
        for j in range(0,4):
            if i != j:
                p[i] = (p[i])*((xe - x[j])/(x[i] - x[j]))

    final = float(0)
    for k in range(0,len(x)):
        final = final + p[k]*y[k]
    
    limpa_interpoladores(p)

    return final


def grafico(x, y, p):
    aux = -1
    fig, ax = plt.subplots()
    
    # xt -> x TOTAL
    # ft -> f(xt)    
    xt, ft = [], []    

    for i in range(0,3001):
        aux = aux + 0.001
        xt.append(aux)
        aux2 = interpoladores_lagrange(aux, x, y, p)        
        ft.append(aux2)
        
    x1 = np.array(x)
    y1 = np.array(y)
    
    x2 = np.array(xt)
    fx = np.array(ft)

    x3 = np.array(x_user)
    y3 = np.array(y_user)  

    primeiros_pontos, = ax.plot(x1, y1, label='Pontos Tabela')
    primeiros_pontos.set_dashes([2, 2, 10, 2])
    segundos_pontos, = ax.plot(x3, y3, label='Pontos Interpolados')    
    segundos_pontos.set_dashes([2, 2, 10, 2])   
    funcao_lagrange, = ax.plot(x2, fx, label='f(x)')

    ax.legend()    
    plt.show()


def main(xe, x, y, p):
    gera_y_user(x_user)
    grafico(x, y, p)
    printa_user(x_user, y_user)


if __name__== '__main__':   
    main(1.1, x, y, p)

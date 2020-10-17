# Hugo de Lacerda Coutinho Neto
# DRE: 118060251
# 15/10/2020


import numpy as np
import matplotlib.pyplot as plt
from math import exp


# Delata1 é o primeiro delta (maiúsculo)
epslon, delta2, kmax = 10**-6, 10**-7, 100


def f(x):
    return x + 0.1 - (0.05*exp((20*x)/(1 + x)))/(1 + 0.1*exp((20*x)/(1 + x)))


def wegstein(a, b, condicao=True):
    fa, fb = f(a), f(b)
    # ai e bi fixos para poder printar no final
    ai, bi = a, b

    if fa*fb > 0:
        # Caso não esteja entre raízes
        print("Entre com novos valores de a e b:")
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))

    y, delta1, k = 1, 1, 0
    while (delta1 > epslon or abs(y) > delta2) and k < kmax:
        multiplicador = fa/(fa - fb)
        x0 = a + multiplicador*(b - a)
        y = f(x0)
        # Se o produto y*fa > 0
        if y*fa > 0:
            fa = y
            a = x0
        # Se o produto y*fa = 0
        elif y*fa == 0:
            break
        # Se o produto y*fa < 0
        else:
            fb = y
            b = x0
        
        delta1 = abs(b-a)
        k = k + 1

    if k < 100:
    # Essa condição é para verificar se convergiu e depois verificar se é interessante
    # printar os valores e retorná-los ou só retorná-los. Caso não haja essa condição,
    # problemas na função grafico na hora de saber as raízes para o intervalo fornecido
        if condicao==True:
            print("Raiz encontrada!")
            print(f"Para [a, b] = [{ai}, {bi}] com {k} interações termos:")
            print(f"| x0 = {x0} | f(x0) = {f(x0)} |")
            return x0
        else:
            return x0
    else:
        # Caso a função diverja...
        print(f"Não fora possível identificar as raízes para [a, b] = [{ai}, {bi}].")
        return None

def grafico(condicao=False):
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
    
    if condicao==False:
        ax.legend()    
        plt.show()  
    else:
        # foi solicitado que indique os pontos das raízes e DRE3/1000. Essa função faz isso
        plt.plot([wegstein(-0.09,-0.1,False), wegstein(0.05, 0.15, False), wegstein(0.3, 0.5, False)], [0, 0, 0],'o', label='Raízes de f(x)')
        plt.plot([0.251],[f(0.251)],'o', label='DRE3/1000')
        ax.legend()
        plt.show()


def main():     
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    wegstein(a, b)
    grafico()
    grafico(True)

if __name__=='__main__':
    main()


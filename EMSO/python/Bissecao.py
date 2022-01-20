# -*- coding: utf-8 -*-
"""
Método de Bisseção para resolução de equações não lineares
@author: roymel
"""

import numpy as np
import matplotlib.pyplot as plt

'Dados'
xi = 0.1 
xs=1
tol=0.01

'Calculos preliminares'
fi = 2*xi + np.log(xi)
fs = 2*xs + np.log(xs)

'Formatando a saída do print no numpy'
np.set_printoptions(formatter={'float': lambda x: "{0:0.4f}".format(x)}) 

'Setando variáveis'
erro = 100
it = 0

'Começo do processo iterativo'
while erro>tol and it<50:   
    it = it+1
    x=(xi+xs)/2
    f=2*x + np.log(x)
    erro = xs-xi
    
    'Gráfico'
    xg = np.linspace(0.1,1)
    fg = 2*xg + np.log(xg)
    zero = 0*xg
    plt.figure(figsize=(6,4))
    plt.title(f'Método Bisseção (iteração {it})')
    plt.plot(xg,fg)
    plt.plot(xg,zero,'--')
    plt.plot([xi,xi],[-2,2])
    plt.plot([xs,xs],[-2,2])
    plt.xlabel('x')
    plt.ylabel('f(x)')
    
    'Apresentando os resultados'
    if it ==1:
        print(['xi', 'fi', 'x', 'f', 'xs', 'fs'])
    print(np.array([xi,fi,x,f,xs,fs,erro]))
    
    'Atualizando variáveis'
    if f*fi>0: 
        xi=x
        fi=f
    else:
        xs=x
        fs=f
    
    
    
    
    

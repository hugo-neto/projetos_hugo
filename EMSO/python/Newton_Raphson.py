# -*- coding: utf-8 -*-
"""
Método de Newton Raphson para resolução de equaõoes não lineares
@author: royme
"""

import numpy as np
import matplotlib.pyplot as plt

'Dados'
x0 = 0.8
tol=0.01

'Formatando a saída do print no numpy'
np.set_printoptions(formatter={'float': lambda x: "{0:0.4f}".format(x)}) 

'Setando variáveis'
erro = 100
it = 0

'Começo do processo iterativo'
while erro>tol and it<50: 
    it = it+1
    f = 2*x0+np.log(x0)
    df = 2+1/x0
    x  = x0-f/df
    erro = abs(x-x0)
        
    'Gráfico'
    xg = np.linspace(0.1,1)
    fg = 2*xg+np.log(xg)
    zero = 0*xg
    plt.figure(figsize=(6,4))
    plt.title(f'Método Newton-Raphson (iteração {it})')
    plt.plot(xg,fg)
    plt.plot(xg,zero,'--')
    plt.plot([x0,x0],[-2,2])
    plt.xlabel('x')
    plt.ylabel('f(x)')
    
    'Apresentando os resultados'
    if it==1: 
        print(['x(k)', 'x(k+1)', 'Erro'])
    print(np.array([x0,x,erro]))
    
    'Atualizando variáveis' 
    x0=x

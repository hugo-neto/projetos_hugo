# -*- coding: utf-8 -*-
"""
Método de Substituição direta para resolução de equações não lineares
@author: roymel
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
    f=np.exp(-2*x0)
    erro = abs(f-x0)
        
    'Gráfico'
    xg = np.linspace(0,1)
    fg = np.exp(-2*xg)
    plt.figure(figsize=(6,4))
    plt.title(f'Método Substituição Direta (iteração {it})')
    plt.plot(xg,fg)
    plt.plot(xg,xg,'--')
    plt.plot([x0,x0],[0,1])
    plt.xlabel('x')
    plt.ylabel('F(x)')
    
    'Apresentando os resultados'
    if it == 1:
        print(['x', 'f', 'Erro'])
    print(np.array([x0,f,erro]))
    
    'Atualizando variáveis'
    x0=f

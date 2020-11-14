from sympy import *
import math

k = Symbol('k', positive=True)
x1 = symbols('x1')
x2 = symbols('x2')
a = symbols('a')


def f(x1, x2):
    return 5*x1*x1 -2*(5*x1 + x2) + 2*x1*x2 + 3*x2*x2 + 251/400


def dx1(x1, x2):
    return 10*x1 + 2*x2 - 10


def dx2(x1, x2):
    return 2*x1 + 6*x2 - 2


def main():
    d0, x, erro = [], [0,0], 10**-6
    x1 = float(input("Digite o valor de x1: "))
    x2 = float(input("Digite o valor de x2: "))
    
    #while norma > erro:
    x[0], x[1] = x1, x2
    d = [-(dx1(x1, x2)), -(dx2(x1, x2))]
    # Acha o mínimos de a
    alfa = solve(diff(f(x[0] + a*d[0], x[1] + a*d[1]), a))
    t1 = x[0] + alfa[0]*d[0]
    t2 = x[1] + alfa[0]*d[1]
    xk = [t1, t2]
    print(xk)
    
    # SE critério atendido ENTÃO FIM
    


if __name__=='__main__':
    main()

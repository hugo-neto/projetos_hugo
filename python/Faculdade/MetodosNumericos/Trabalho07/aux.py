from sympy import *
import math


pi = Symbol('pi', positive=True)
a = Symbol('a', positive=True)
A = Symbol('A', positive=True)
B = Symbol('B', positive=True)
c = Symbol('c', positive=True)
k = Symbol('k', positive=True)
m = Symbol('m', positive=True)
L = Symbol('L', positive=True)
h = Symbol('h', positive=True)
x1 = symbols('x1')
x2 = symbols('x2')


def f(x1, x2):
    return 5*x1*x1 -2*(5*x1 + x2) + 2*x1*x2 + 3*x2*x2 + 251/400


def main():
    x1 = float(input("Digite um valor para x1: "))
    x2 = float(input("Digite um valor para x2: "))
    x = [1,1]
    d0 = -[diff(f(x1, x2), x1), diff(f(x1, x2), x2)]
    print(d0)




if __name__=='__main__':
    main()

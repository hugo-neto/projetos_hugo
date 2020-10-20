from sympy import *
from math import log

k = Symbol('k', positive=True)
L = Symbol('L', positive=True)
n = Symbol('n', positive=True)
pi = Symbol('pi', positive=True)
Z = Symbol('Z', positive=True)
a0 = Symbol('a0', positive=True)

x = symbols('x')

init_printing(use_unicode=True)

valor = integrate((-2*(k/L)*sin(n*pi*x/L)*sin(n*pi*x/L)*x), (x,0,L)).doit()
print(valor)
# Resolve a integral com constante k

funcao = x**2*(2*(Z/a0)**1.5*exp(-Z*x/a0))**2

print(diff(funcao, x))

solve(x**2 - 1)
# Resolve essa eq. de segundo grau

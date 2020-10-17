from sympy import *
from math import log

k = Symbol('k', positive=True)

x = symbols('x')
init_printing(use_unicode=True)

valor = integrate((x*x*exp(k*x)), x)
print(valor)
# Resolve a integral com constante k

solve(x**2 - 1)
# Resolve essa eq. de segundo grau

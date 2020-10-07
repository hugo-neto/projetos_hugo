from sympy import *
from math import log

x = symbols('x')

init_printing(use_unicode=True)

diff(x**3)
# deve sair 3*x**2

valor = Integral(((A/x + B + C * x + D * x ** -3)), (x,400,600)).doit()
# Resolve a integral definida


from sympy import *
import math


v = Symbol('v', positive=True)
C = Symbol('C', positive=True)
c = Symbol('c', positive=True)
m = Symbol('m', positive=True)
M = Symbol('M', positive=True)
g = Symbol('g', positive=True)
A = Symbol('A', positive=True)
z0 = Symbol('z0', positive=True)
L = Symbol('L', positive=True)
n = Symbol('n', positive=True)
k = Symbol('k', positive=True)
U0 = Symbol('U0', positive=True)
h = Symbol('h', positive=True)
a = Symbol('a', positive=True)
R = Symbol('R', positive=True)
b = Symbol('b', positive=True)
pi = Symbol('pi', positive=True)
ro = Symbol('ro', positive=True)

x = symbols('x')
r = symbols('r')
y = symbols('y')

init_printing(use_unicode=True)

funcao_diff = U0*(1+x/L)

print(diff(funcao_diff, x, 1))
# Aplica o operador diferencial df(x)/dx na função n vezes (último número)

funcao_diff = -U0*(y/L)

print(diff(funcao_diff, y, 1))
# Aplica o operador diferencial df(x)/dx na função n vezes (último número)


funcao = 2*pi*U0*U0*r*((1-r*r/(R*R))**2)
valor = integrate((funcao), (r, 0, R)).doit()

print(f"Valor da funcao 1 é: {valor}")

funcao = C*C*ro*r**(2*n-1)
valor = integrate((funcao), (r)).doit()

print(f"Valor da funcao 2 é: {valor}")

calculo = (1.5 +3*3.1415*9.81/4)/((-5*3.1415*9.81*0.5 + 9.81*3.1415*0.5*(9*0.01)**2)*10**3)
print(f"Valor do cálculo é: {calculo}")

# Resolve a integral com constante k

funcao_diff = C*y*(2*h - y)

print(diff(funcao_diff, y, 1))
# Aplica o operador diferencial df(x)/dx na função n vezes (último número)

print(solve(((1-x)*(1-x))+1))
# Resolve essa eq. de segundo grau

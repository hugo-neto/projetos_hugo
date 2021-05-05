#PACOTE SYMPY PRECISA ESTAR INSTALADO!

from sympy import *
import math
#Logarítmo natural math.log()


# Símbolos que podem ser utilizados no processo de integração
# e que não são rejeitados pelo python
v = Symbol('v', positive=True)
C = Symbol('C', positive=True)
c = Symbol('c', positive=True)
m = Symbol('m', positive=True)
M = Symbol('M', positive=True)
g = Symbol('g', positive=True)
E = Symbol('E', positive=True)
z0 = Symbol('z0', positive=True)
L = Symbol('L', positive=True)
n = Symbol('n', positive=True)
k = Symbol('k', positive=True)
U0 = Symbol('U0', positive=True)
h = Symbol('h', positive=True)
a = Symbol('a', positive=True)
a0 = Symbol('a0', positive=True)
b = Symbol('b', positive=True)
R = Symbol('R', positive=True)
b = Symbol('b', positive=True)
u = Symbol('u', positive=True)
pi = Symbol('pi', positive=True)
ro = Symbol('ro', positive=True)


#Variáveis que podem ser integradas
x = symbols('x')
r = symbols('r')
t = symbols('t')
y = symbols('y')

# Código padrão. Não sei para que serve
init_printing(use_unicode=True)


funcao_diff = U0*(1+x/L)

print(diff(funcao_diff, x, 1))
# Aplica o operador diferencial df(x)/dx na função n vezes (último número)
# Pode-se ser alterado dx para dr, dt, dy....

funcao_diff = -U0*(y/L)

print(diff(funcao_diff, y, 1))
# Aplica o operador diferencial df(x)/dx na função n vezes (último número)

funcao = ((1+x)**2)/((1-x)**2)
valor = integrate((funcao), (x)).doit()


print(f"Valor da funcao 1 é: {valor}")


funcao = k*x*x*exp(-k*x)
valor = integrate((funcao), (x, 0, math.inf)).doit()
# Integra a 'função' com respeito a x no intervalo a, b (constantes quaisquer)
# em: (...)(x, a, b)).doit()


print(f"Valor da funcao 2 é: {valor}")

funcao = (2/63)*(10 - x)
valor = integrate((funcao), (x, 3, 7.5)).doit()

print(f"Valor da funcao 3 é: {valor}")

calculo = (1.5 +3*3.1415*9.81/4)/((-5*3.1415*9.81*0.5 + 9.81*3.1415*0.5*(9*0.01)**2)*10**3)
print(f"Valor do cálculo é: {calculo}")

# Resolve a integral com constante k

#*4*math.pi
psi = ((1/a0)**(1.5))*(2-r/a0)*exp(-r/(2*a0))
funcao_diff = r*r*psi*psi/(8)

print(diff(funcao_diff, r, 1))
# Aplica o operador diferencial df(x)/dx na função n vezes (último número)

keq, Conc = 1.42*(10**-5), (10**-5)
print(f"Keq = {keq}; Concentração = {Conc}")

tudo = funcao_diff

print(solve(tudo, r))
# Resolve essa eq. de segundo grau

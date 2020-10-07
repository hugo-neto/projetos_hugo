# Criador: Hugo de Lacerda Coutinho Neto
# Termodinâmica
# DRE: 118060251
# 08/10/2020


import math

# nome = input("Qual é o nome da substância: ")

# print("Digite o valor de:")
# fator_acentrico = float(input("Fator acêntrico: "))
# Tc = float(input("Temperatura Crítica em Kelvin [K]: "))
# Pc = float(input("Pressão Crítica em bar [bar]: "))
# Zc = float(input("Zc: "))

nome, fator_acentrico, Tc, Pc, Zc  = "Hexano", 0.3, 507.6, 30.25, 0.266

Vl, Vv, R = 0, 0, 83.1451

# H, S, G líquido e H, S, G vapor residual
Hlr, Hvr = 0,0
Slr, Svr = 0,0
Glr, Gvr = 0,0

# Unidade R = [bar.cm3/mol.K]
# Unidade Pc = [bar]
# Unidade Tc = [k]


def omegaA():
    return 0.66121 - 0.76105 * Zc


def omegaB():
    return 0.02207 + 0.20868 * Zc


def r():
    r = 1
    r = r + (0.57765 - 1.8708 * Zc)/omegaB()
    return r


def gama():
    # ri = r = r()
    ri = r()
    termo = ri*ri + 4*ri - 4
    gamaf = (ri - math.sqrt(termo))/2
    return gamaf


def epslon():
    # ri = r = r()
    ri = r()
    termo = ri*ri + 4*ri - 4
    epslonf = (ri + math.sqrt(termo))/2
    return epslonf


def kapa():
    x = fator_acentrico * Zc
    k = 0.46283 + 3.5823*x + 8.19417*x*x
    return k


def ac():
    termo, ac = R * Tc, omegaA()
    return ac * (termo ** 2)/Pc


def a(T):
    termo2 = alfa(T)
    theend = ac() * termo2
    return theend


def b():
    bf = omegaB()
    bf = bf*(R * Tc)/Pc
    return bf


def volume_molar_liquido(V, P, T):
    
    # Cálculo de epslon e gama da fórmula interativa geral
    # Fórmula interativa geral = eq. de estado em função 
    # da escolha de cada método
    eps, gam = epslon(), gama()

    # Cálculo do Volume pelo método interativo geral
    termo = (R*T - P*(V - b()))/a(T)
    Vfl = b() + (V + gam * b())*(V + b() * eps)*(termo)

    return Vfl


def volume_molar_vapor(V, P, T):
    Vfv = R*T/P
    
    # Cálculo de epslon e gama da fórmula interativa geral
    # Fórmula interativa geral = eq. de estado em função 
    # da escolha de cada método
    eps, gam = epslon(), gama()
    
    termo = (V - b())/((V + gam*b())*(V + eps*b()))
    Vfv = Vfv + b() - (a(T)/P)*(termo) 
    return Vfv


def vol_molar_geral(P, T, convergencia = 0.0001):
    # Começando com líquido
    global Vl, Vv 
    Vl, Vv = b(), R*T/P

    while abs(Vl - volume_molar_liquido(Vl,P,T)) >= convergencia:
        Vl = volume_molar_liquido(Vl,P,T)
    
    contador = 0
    while (abs(Vv - volume_molar_vapor(Vv,P,T)) >= convergencia) and (contador <= 1000):
        contador = contador + 1
        Vv = volume_molar_vapor(Vv,P,T)
    if contador >= 999:
        Vv = Vl

def alfa(T):
    Tr = T/Tc
    final = (1 + kapa()*(1 - math.sqrt(Tr)))**2
    return final


def alfalinha(T):
    Tr = T/Tc
    raiz = math.sqrt(Tr) 
    termo = ((1 + kapa())/raiz)
    return kapa()*(kapa() - termo)


def alinha(T):
    final = (ac()/Tc)*(alfalinha(T))
    return final


def fi(V):
    final = 1/b()
    final = final*(1/( epslon() - gama() ))
    termo = (V + epslon()*b())/(V + gama()*b())
    return final*math.log(termo)


def entalpia_r(P, T):
    global Hlr, Hvr
    Hlr = P*Vl - R*T + (T*alinha(T) - a(T))*fi(Vl)
    Hvr = P*Vv - R*T + (T*alinha(T) - a(T))*fi(Vv)
    

def entropia_r(P, T):
    global Slr, Svr
    termo1 = P*(Vl-b())/(R*T)
    termo2 = P*(Vv-b())/(R*T)
    Slr = alinha(T)*fi(Vl) + R*math.log(termo1)
    Svr = alinha(T)*fi(Vv) + R*math.log(termo2)


def gibs(T):
    global Glr, Gvr
    Glr = Hlr - T*Slr
    Gvr = Hvr - T*Svr


def printa():
    print("Para a substância " + nome + " teremos:")
    print(f"Volume de Líquido: {Vl} cm³/mol")
    print(f"Volume de Gás: {Vv} cm³/mol")
    print(f"Entropia residual de Líquido: {Slr}")
    print(f"Entropia residual de Gás: {Svr}")
    print(f"Hentalpia resitual de Líquido: {Hlr}")
    print(f"Hentalpia resitual de Gás: {Hvr}")
    print(f"Energia Livre de Gibs resitual de Líquido: {Glr}")
    print(f"Energia Livre de Gibs resitual de Gás: {Gvr}")
    
    
def main():
    P = float(input("Digite a Pressão em bar: \n"))
    T = float(input("Digite a Temperatura em Kelvin: \n"))
    
    vol_molar_geral(P, T)
    entalpia_r(P, T)
    entropia_r(P, T)
    gibs(T)
    printa()


if __name__ == '__main__':
    main()

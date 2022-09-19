#!/usr/bin/python

# =========================================================
#
# Idealizado por Hugo de Lacerda Coutinho Neto
# 18/Setembro/2022
# Automatização de funções recorrentes em OP2
#
# =========================================================


from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve, root


def plotar(tau, func):
    plt.plot(tau, func(tau))
    plt.xlabel("tau")
    plt.ylabel("expression value")
    plt.grid()
    plt.show()


# Funcao de logaritmo neperiano (só para facilitar as notações)
def ln(valor):
    return np.log(valor)


class Calculo:
    def __init__(self):
        pass

    def Derivada(self, funcao, x):
        return diff(funcao, x)


class Termodinamica:
    def __init__(self, A=None, B=None, C=None):
        # Parametros para Antoine
        self.A = A
        self.B = B
        self.C = C
        # Constante Universal dos gases J/mol.K
        self.R = 8.31447

    # Eq. de Antoine com T [°C] P [kPa]
    def SolverAntoine(self, P=None, T=None):
        # Para chamar, fixe P OU T e o resultado sera fornecido
        # Ex.: Termodinamica(A, B, C).SolverAntoine(P=100)
        if P==None:
            return np.exp(self.A - self.B/(T+self.C))
        elif T==None:
            T = 50
            return fsolve(lambda T : ln(P) - self.A + self.B/(T+self.C), T)[0]
    
    # Calcula os Deltas ij e ik da Eq. do Virial
    def SolverDeltaVirial(self, i, const, MatrizB):
        return 2*MatrizB[i][const] - MatrizB[i][i] - MatrizB[const][const]

    # Calcula o valor de B do Virial
    def SolverB_Virial(self, y, MatrizB, B=0):
        if sum(y) != 1: return

        # Pega o numero de componentes com base no vetor y
        NumeComp = len(y)
        for i in range(0, NumeComp):
            for j in range(0, NumeComp):
                B = B + y[i]*y[j]*MatrizB[i][j]
        return B

    def ConverteSi(T=None, P=None):
        # T vazia ele converte P
        if T==None:
            pass
        elif P==None:
            pass
    
    def Z_Virial(self, P, T, B):
        # P em Pa, T em K
        return 1 + B*P/(self.R*T)

    # Calcula Coeficiente de Fugacidade para gases com base em Virial
    def SolverFugacidade_Virial(self, P, T, y, MatrizB, CoefFug=list(), \
                            UnitT='k', UnitP='Pa', UnitB='m3/mol'):
        if sum(y) != 1: return
        # Obtem o numero de componentes com o vetor y
        NumeComp = len(y)
        
        # T [°K] P [Pa]
        if UnitT == 'C': T = T + 273.15
        
        if UnitP == 'bar':
            P = (10**5)*P
        elif UnitP == 'Pa':
            P = P
        else:
            print("User Pressao em Pa")
            return

        PRT = (P/(self.R*T))
        
        for k in range(0, NumeComp):
            LnFugacidade = PRT*(MatrizB[k][k])
            for i in range(0, NumeComp):
                for j in range(0, NumeComp):
                    LnFugacidade = LnFugacidade + 0.5*(PRT)*(y[i])*(y[j])* \
                                    (2*(self.SolverDeltaVirial(i, k, MatrizB)) - self.SolverDeltaVirial(i, j, MatrizB))
            CoefFug.append(np.exp(LnFugacidade))
        
        print("")
        print("Coeficientes de fugacidade calculados para GASES")
        print(f"Unidade P: {UnitP} Unidade T: {UnitT} Unidade B: {UnitB}")
        return CoefFug


    # Calcular a Fugacidade em funcao do estado físico e o valor de xi
    def SolverFugacidade(self, EstadoFisico, *Args):
        # Modelo para espécie gasosa ou vapor
        if EstadoFisico=='Gás' or EstadoFisico=='Gas' or EstadoFisico=='Vapor':
            # Args = [0, 1,     2]
            # Args = [P, yi, CoefFug]
            return Args[0]*Args[1]*Args[2]
        
        # Modelo para espécies líquidas
        elif EstadoFisico=='Liquido' or EstadoFisico=='Líquido':
            # Solução Ideal Coeficiente de Atividade = 1
            # P baixa fugacidade = Henry ou fugacitade = P,sat

            # Args = [  0,       1   , 2,  3]
            # Args = [f ou H, CoefAti, xi, T]
            if Args[2] >= 0.5 and Args[2] <= 1.0:
                return Args[0]*Args[1]*Args[2]
            
            elif Args[2] > 0 and Args[2] < 0.5:
                return self.SolverAntoine(T=Args[3])*Args[1]*Args[2]
            
            else:
                print("Verifique o valor de xi")


def main():
    # Gera a Classe com os parametros da Eq. de Antoine
    Termo = Termodinamica(14.3145, 2756.22, 288.06)
    
    # Resolve a Equacao de Antoine com T em C
    print(Termo.SolverAntoine(T=50))
    
    MatrizB = [ [-276*(10**-6), -466*(10**-6)], 
                [-466*(10**-6), -809*(10**-6)] ]
    y = [0.5, 0.5]
    
    print(Termo.SolverFugacidade_Virial(2, 75, y, MatrizB, UnitT='C', UnitP='bar'))
    
    print(Termo.SolverB_Virial(y, MatrizB))
    # P em Pa e T em K
    print(Termo.Z_Virial(2*100000, 273.15+75, Termo.SolverB_Virial(y, MatrizB)))

    A = Symbol('A', positive=True)
    B = Symbol('B', positive=True)
    C = Symbol('C', positive=True)
    
    x1 = symbols('x1')
    x2 = symbols('x2')
    x3 = symbols('x3')
    
    n1 = symbols('n1')
    n2 = symbols('n2')
    n3 = symbols('n3')

    n = n1+n2
    funcao1 = ((n))*n1*n2*(A + B*n1/(n))/((n)**2)
    print(Calculo().Derivada(funcao1, n1))

    funcao2 = (x1*x2)*(A*x2 + B*x1)
    print(Calculo().Derivada(funcao2, x1))

    funcao3 = (x1*x2)*(A*x2 + B*x1)
    print(Calculo().Derivada(funcao3, x2))


# Use the numerical solver to find the roots
if __name__ == '__main__':
    main()
    


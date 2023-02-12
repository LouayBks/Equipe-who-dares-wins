# -*- coding: utf-8 -*-
import numpy as np


c = [1,2,0,0]
A = [
    [1,4,1,0],
    [2,1,0,1],
    
]
b = [8,3]
def conversionTableau(c, A, b):
    xb = [eq + [x] for eq, x in zip(A, b)]
    z = c + [0]
    return xb + [z]

def optimisable(tableau):
    z = tableau[-1]
    return any(x > 0 for x in z[:-1])
import math

def pivot(tableau):
    z = tableau[-1]
    column = next(i for i, x in enumerate(z[:-1]) if x > 0)
    
    restrictions = []
    for eq in tableau[:-1]:
        el = eq[column]
        restrictions.append(math.inf if el <= 0 else eq[-1] / el)
        
    if (all([r == math.inf for r in restrictions])):
        raise Exception("Le problème linéaire est non borné.")

    row = restrictions.index(min(restrictions))
    return row, column
def pasPivot(tableau, pivotPosition):
    newTableau = [[] for eq in tableau]
    
    i, j = pivotPosition
    pivotValue = tableau[i][j]
    newTableau[i] = np.array(tableau[i]) / pivotValue
    
    for eq_i, eq in enumerate(tableau):
        if eq_i != i:
            multiplier = np.array(newTableau[i]) * tableau[eq_i][j]
            newTableau[eq_i] = np.array(tableau[eq_i]) - multiplier
   
    return newTableau
def estBasique(column):
    return sum(column) == 1 and len([c for c in column if c == 0]) == len(column) - 1

def solution(tableau):
    columns = np.array(tableau).T
    solutions = []
    for column in columns[:-1]:
        solution = 0
        if estBasique(column):
            one_index = column.tolist().index(1)
            solution = columns[-1][one_index]
        solutions.append(solution)
        
    return solutions
def simplexe(c, A, b):
    tableau = conversionTableau(c, A, b)

    while optimisable(tableau):
        pivotPosition = pivot(tableau)
        tableau = pasPivot(tableau, pivotPosition)

    return solution(tableau)
slt = simplexe(c, A, b)
valeurOpt=(np.dot(slt,c))
print('La solution est:')
for i in range (len(slt)):
    print('x',i+1,'*= ',slt[i])
print('La valeur optimale est Z*=',valeurOpt)
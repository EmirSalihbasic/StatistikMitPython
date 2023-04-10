# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 03:32:26 2023

@author: Korisnik
"""

# =============================================================================
# ZIEHUNGEN UND UMSORTIERUNGEN
# =============================================================================

#Binomialkoeffizient und Kombination ohne Zurücklegen    
   
import math as m
def binomialkoeffizient (n,k):
    return int (m.factorial(n) / (m.factorial(k) * m.factorial (n-k)))
print (binomialkoeffizient(49, 6))

#Kombination mit Zurücklegen (mit wiederholung)

import math as m
def kombinationen (n,k):
    return int (m.factorial(n+k-1) / (m.factorial(k) * m.factorial (n-k)))
print (kombinationen(6, 2))

#Variation ohne Zurücklegen

import math as m
def variationen (n,k):
    return int (m.factorial(n) / m.factorial(n-k))
print (variationen(6, 2))

# permutationen
import math as m
def permutationen (n,k):
    divisor = 1
    for i in k:
        divisor = divisor * m.factorial (1)
        print(m.factorial (n), divisor)
        return int (m.factorial (n)/ divisor)
print (permutationen(3,[2]))
print (permutationen(5,[2, 2]))
print (permutationen(5,[2,2,6]))

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 03:34:40 2023

@author: Korisnik
"""


import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print (numpy.outer(A, B))

#max un min

zufallszahlen = (10, 5, 15, 9,11,15,13,12)
print("Maximum", max(zufallszahlen))
print("Minimum", min(zufallszahlen))


#built-in funktion min und max
mx = 0
mn = 0
zufallszahlen = (10, 5, 15, 9,11,15,13,12)
for p in zufallszahlen:
   if p > mx:
      mx = p
print("maximum", mx)
      
mn = mx      
for p in zufallszahlen:
    if p < mn:
        mn = p
        print("minimum", min)
        
 # Was kommt am häufigsten vor?       
import statistics as s 
zahlen = (3, 11, 4, 7, 10)     
namen = ("Kevin", "George", "Andreas", "Maria", "George")   
print (s.mode(zahlen))
print (s.mode (namen))


# Anzahl der Elemente (length)
num = (1 , 3, 5, 8)
print(len(num))

#Der Mittelwert (primzahlen/anzahl der Elemente)
m=0
primzahlen = [10, 5, 15, 9,11,15,13,12]
for p in primzahlen :
    m=m+p
print(len(primzahlen))    
print(m)
print(m/len(primzahlen))

# Die Fakultät
import math as m
print (m.factorial(5))

#Der Zentralwert (median)

import statistics as s
zahlen1 = [9, 2, 3, 15, 5, 7, 311, 13, 147, 419, 23, 291, 31, 37]
zahlen2 = [9, 2, 3, 15, 5, 7, 311, 13, 147, 419, 23, 291, 31, 754, 37]

print("Originaldatenstruktur 1", zahlen1)
print("Datenstruktur 1 sortiert: ", sorted(zahlen1))
print("Anzahl Elemente Datenstruktur 1: ",len(zahlen1))
print("Median Datenstruktur 1: ",s.median(zahlen1))
print("Median_low Datenstruktur 1: ",s.median_low(zahlen1))
print("Median_high Datenstruktur 1: ",s.median_high(zahlen1))
print("*" * 30)
print("Originaldatenstruktur 2", zahlen2)
print("Datenstruktur 2 sortiert: ", sorted(zahlen2))
print("Anzahl Elemente Datenstruktur 2: ",len(zahlen2))
print("Median Datenstruktur 2: ",s.median(zahlen2))
print("Median_low Datenstruktur 2: ",s.median_low(zahlen2))
print("Median_high Datenstruktur 2: ",s.median_high(zahlen2))

#Stochasticher (Zufallprozess)
import time
i = 0
zz = []
while i < 10:
    z = int(time.time() * 9923) % 100
    if z in zz:
        continue
    zz.append(z)
    i=1+i
    print(zz)
    
import random as r
r.seed()
i=0
while i < 10:
    print(r.randrange(100))
    i = i + 1
    print("*" * 20)
zufallszahlen = [100,2,88,143,3,15,47]
i=0
while i > 10:
    r.shuffle(zufallszahlen)
    print(zufallszahlen)
    i = i + 1
    
    



import numpy as np
prim = np.array([2,3,5,7, 11,13,17])
print("Das Array", prim)
print("Die Array-Groesse", prim.size)
print("Datentyp der Array-Elemente",  prim.dtype)
print("*" * 30)

mehrdimArray = np.array([(1.5,2,3), (4,5,6), (7,11,33,54)])
print("Das mehrdimensionale Array\n", mehrdimArray)
print("*" * 30)

nullinitArray = np.zeros( 49 )
print("Das nullinitialisierte Array - eindimensional\n", nullinitArray)
print("*" * 30)

nullinitArrayMehrDim1 = np.zeros( (10,4) )
print("Das nullinitialisierte Array - zweidimensional\n", nullinitArrayMehrDim1)
nullinitArrayMehrDim2 = np.zeros( (2,5,4,4) )
print("Das nullinitialisierte Array - 4 Dimensionen\n", nullinitArrayMehrDim2)

print("*" * 30)

bereich1 = np.arange( 10, 30 )
print("Das Array mit einem Wertebereich zwischen 10 und 30 (exklusive) und Defaultschritten\n", bereich1)
print("*" * 30)
bereich2 = np.arange( 10, 30, 3 )
print("Das Array mit einem Wertebereich und Schritten mit dem Abstand 3\n", bereich2)
print("*" * 30)
bereich3 = np.arange( 1, 4, 0.3 )
print("Das Array mit einem Wertebereich zwischen 1 und 4 und Schritten mit einem Abstand 0.3\n", bereich3)
print("*" * 30)

# Umdimensionieren von Arrays
aDim1 = np.arange(100)
print("Das originale Array (eindimensional)\n", aDim1)
print("*" * 30)
aDim2 = aDim1.reshape(10,10)
print("Das Array umdimensioniert\n", aDim2)
print("*" * 30)

zufallszahlen = np.array([100, 2,88, 143, 3, 15, 47, 11, 13, 97, 19, 23, 29, 31])
print("Maximum:", np.max(zufallszahlen))
print("Minimum:", np.min(zufallszahlen))
print("Mittelwert:", np.mean(zufallszahlen))
print("Zentralwert:", np.median(zufallszahlen))

print("*" * 30)
zufallszahlen2 = zufallszahlen.reshape(2,7)
print("Das Array umdimensioniert\n", zufallszahlen2)
print("*" * 30)
print("Maximum:", np.max(zufallszahlen2))
print("Minimum:", np.min(zufallszahlen2))
print("Mittelwert:", np.mean(zufallszahlen2))
print("Zentralwert:", np.median(zufallszahlen2))

print("*" * 30)


import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,5,0.1);
y=np.sin(x)
plt.plot(x,y)
plt._show()
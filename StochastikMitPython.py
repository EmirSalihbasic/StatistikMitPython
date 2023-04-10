# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 03:31:14 2023

@author: Korisnik
"""

# =============================================================================
# STOCHASTIK MIT PYTHON
# =============================================================================
#Wahrscheinlichkeitsverteilung

import statistics as s 
zahlen = (8,7,9,10,6)      

print(s.variance(zahlen))
print(s.pvariance(zahlen))

   
print(s.variance(zahlen, s.mean(zahlen)))
print(s.pvariance(zahlen, s.mean(zahlen)))
                  
print(s.stdev(zahlen))
print(s.pstdev(zahlen))    

#Binomialverteilung und Bernoulli-prozesse

import math as m
import matplotlib.pyplot as plt

n = 10 # Zahl der Versuche
p = 0.5 # Wahrscheinlichkeit für Erfolg
k = 0  # Getestete Anzahl der Erfolge
P = list()
i = 0
while k <= n:
    i = m.factorial(n) / (m.factorial(k) * m.factorial(n - k) ) * m.pow(p,k) * m.pow(1 - p, n - k)
    print(i)
    P.append(i)
    k = k + 1
print(P)
plt.plot(P)
plt._show()              

#Das Gesetz der Großen Zahlen
import math as m
import random as r
import matplotlib.pyplot as plt
verfuegbareZahlen = list(range(1,50))
ziehungen = list()
counter = list()
i = 0
while i < 50:
    counter.append(0)
    i = i + 1
def ziehung():
    return r.sample(verfuegbareZahlen, 6)
i = 0
while(i < 100000):
    ziehungen.append(ziehung())
    i = i + 1
#print (ziehungen)
print("Ziehungen beendet", "*" * 30)
for e in ziehungen:
    #print(e)
    for f in e:
        #print(f)
        j = 1
        while j < 50:
            if f == j:
               counter[j] = counter[j] + 1
            j = j + 1
counter.remove(0)
print(counter)
plt.axis([0, 50, 1000, 25000])
plt.plot(counter)
plt.show()



mu = 0
variance = 1
sigma = m.sqrt(variance)
x = np.linspace(mu - 5* sigma, mu + 5 * sigma, 100)
plt.plot(mlab.normpdf(x, mu, sigma))
plt.show()

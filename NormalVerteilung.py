# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 03:29:44 2023

@author: Korisnik
"""

#normalverteilung 1
import math as m


def nv(x,mu,sigma):
    return (1 / (sigma * m.sqrt(2 * m.pi) )) * m.pow(m.e, -0.5 * m.pow(((x - mu)/sigma), 2))

#normalverteilung 2
import math as m
import random as r
import matplotlib.pyplot as plt
ziehungen = list()
def ziehung():
    mu = 10
    sigma = 0.1
    return r.gauss(mu, sigma)
i = 0
while(i < 100):
    ziehungen.append(ziehung())
    i = i + 1
print("Ziehungen beendet", "*" * 30)
print(ziehungen)
plt.plot(ziehungen)
plt.show()

#normalverteilung 3
import math as m
import numpy as np
import matplotlib.pyplot as plt
mu = 10
sigma = 0.1
ziehungen = np.random.normal(mu, sigma, 100)
print("Ziehungen beendet", "*" * 30)
print(ziehungen)
plt.plot(ziehungen)
plt.show()

#normalverteilung 4
import math as m
import matplotlib.pyplot as plt
ziehungen = list()
def nv(x,mu,sigma):
    return (1 / (sigma * m.sqrt(2 * m.pi) )) * m.pow(m.e, -0.5 * m.pow(((x - mu)/sigma), 2))
i = -1
while(i < 1):
    ziehungen.append(nv(i,0,1))
    i = i + 1/100
print("Ziehungen beendet", "*" * 30)
plt.plot(ziehungen)
plt.show()


#normalverteilung 5
import math as m
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
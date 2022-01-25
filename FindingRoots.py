#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 19:51:11 2021

@author: loaner
"""

import numpy as np
#import math
import matplotlib.pyplot as plt
from pylab import clf
from scipy.optimize import fsolve

clf()

m = 9*(10**(-31))#kilograms
V = 1.6*(10**(-16)) #converted it to  joules???
a = 0.529*(10 **(-10))#meter
h = 6.63*(10**(-34))/(2*np.pi)#plancks constant

k2 = 2*m*(a**2)*V/(h**2)

x = np.linspace(4,7,1000)

def f(x):
    output = (x * (1/np.tan(x))) + np.sqrt(k2 + (x**2))
    return float(output)

f2 = np.vectorize(f)

plt.plot(x, f2(x))

plt.axhline(y = 0, color = "black")
#plt.axvline(x = 5.77, color = "black")

#plt.show()

#estimate = float(5.75)
estimate = np.array([5.7,5.8])

print(fsolve( f , 5.77))

print(fsolve( f , 5.77 + np.pi))


i = 0

while i < 2:
    
    s = fsolve( f , 5.77 + (i*np.pi))
    
    #plt.axvline(x = s, color = 'black')
    
    
    i = i +1
    
plt.ylim(-5,5)  
    
plt.show()
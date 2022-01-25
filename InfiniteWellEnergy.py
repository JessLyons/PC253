#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 15:31:21 2022

@author: jessielyons
"""
import math
import numpy as np
import matplotlib.pyplot as plt

a = 0.529E-10 #meters

V = 1.602E-16 #joules

h = 6.626E-34 #joule second (h bar)





def function (m,n):
    
    k = math.sqrt(2.0*m*(a**2)*V/(h**2))
    
    x = list(np.linspace(0,5,100000))
    
    energy = 0
    i = 0
    for s in x:
        if(math.sin(s) != 0):
            solve_s = s*(1/math.sin(s))
            if(solve_s ==k):
                i= i+1
                if(i==n):
                    energy = V*math.cos(s)
                    break
    return energy


mass = list(np.linspace(0,1.7E-27))

energy_1 = function(mass,1)

plt.plot(mass, energy_1)






#k = math.sqrt(2*(a**2)*V/(h**2)) # left out mass






#x = list(np.linspace(0,5,100000))

#s = x[x*(1/math.sin(x)) == k]

#print(s.shape)




from pylab import figure, cm

import numpy as np
import matplotlib.pyplot as plt

def function(x):
    y = 1.0 * x**5.0
    return y

x = np.arange(0.0, 3.0, 0.1)

y = function(x)

fig = figure(num=None, figsize=(6, 10), dpi=80, facecolor='w', edgecolor='k')

plt.plot(x,y)

plt.title('f(x)')
plt.xlabel('x')
plt.ylabel('y')

#plt.grid()

plt.savefig("function.png", bbox_inches='tight')

plt.show()
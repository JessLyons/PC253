#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 11:07:50 2021

@author: loaner
"""
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

def Gaussian(x,sigma):
    return (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-((x)**2)/(2*(sigma**2)))

def probability(x0,x,sigma):
    value,error = quad(Gaussian, x0, x, args = sigma)
    return value

print(probability(-1,1,1))

sigmas = np.linspace(0,10,100)

print()
for x in sigmas:
    diff = 0.682689492137086 - probability(-x,x,x)
    if diff != 0:
        d = str(diff)
        sig = str(x)
        print("Difference is" + d + "for sigma" + sig)
print()

probs = []

for x in sigmas:
    p = probability(-x,x,x)
    probs.append(p)

plt.plot(sigmas,probs)

plt.ylim( 0.682689492137085, 0.682689492137087)

# all values are close to 0.682689492137086


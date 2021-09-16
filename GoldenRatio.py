#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 14:47:50 2021

@author: loaner
"""

import matplotlib.pyplot as plt
import numpy as np
import math

def fibonacci(n):
    sequence = [1,1]
    i = 1
    while i < (n-1):
        fib_num = sequence[i] + sequence[i-1]
        sequence.append(fib_num)
        i = i + 1
    return sequence


n = 50

print(fibonacci(n))
sequence = fibonacci(n)


x = np.linspace(1,n-1,n-1)
#print(x)

#ratio = []
#for l in x:
   # R = sequence[int(l)]/sequence[int(l)-1]
    #ratio.append(R)

#plt.plot(x,ratio,linewidth = 2, color = 'b')
#plt.title('Golden Ratio Convergence')
#plt.xlabel('Number of Terms')
#plt.ylabel('Ratio')

gr = (1 + math.sqrt(5))/2
#plt.axhline(y=gr, color='r', linestyle='--')
#plt.axvline(x = 7, color = 'grey', linestyle = '--')
#plt.ylim(1.6,1.625)
#plt.show()


#doing array operation to optimize time instead of loop
faster = np.divide(sequence[1::1],sequence[:-1:1])

#plt.plot(x,faster)
#plt.title('The faster way')
#plt.show()

plt.clf()
#errror
error = np.abs(faster - gr)
plt.semilogy(x,error)
plt.title("error")
plt.show()

"""
I would say that it converges at the 7th term because this is where the 
graph is no longer visibly "bumped". When I zoom in, this is no longer 
the case but the seventh term is still less than a hundreth away from 
the golden ratio.

"""
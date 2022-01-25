#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 10:14:14 2022

@author: jessielyons
"""
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import math

## set initial conditions and parameters
g = 9.81            # acceleration due to gravity



theta0 = 10.0
l = 10.0
omega0 = math.sqrt(g/l)
beta = 0.5
gamma = 1.47
frequency = (2/3)*omega0


## define function to compute f(X,t)
def f_func(state,time):
    f = np.zeros(2)    # create array to hold f vector
    f[0] = state[1] # angular velocity
    f[1] = -2*beta*state[1] + (-g/l)*math.sin(state[0])+ gamma*(-g/l)*math.cos(frequency*time)  # angular acceleration due to gravity
    return f

## set initial state vector and time array
t0 = 0.
X0 = [theta0, omega0]        # set initial state of the system
tf_str = input("Enter final time: ")
tau_str = input("Enter time step: ")
tf = float(tf_str)
tau = float(tau_str)

# create time array starting at t0, ending at tf with a spacing tau
t = np.arange(t0,tf,tau)

## solve ODE using odeint
X = odeint(f_func,X0,t) # returns an 2-dimensional array with the
                        # first index specifying the time and the
                        # second index specifying the component of
                        # the state vector

# putting ':' as an index specifies all of the elements for
# that index so x, y, vx, and vy are arrays at times specified
# in the time array

theta = X[:,0]
omega = X[:,1]

plt.figure(1)
plt.clf()

plt.plot(t,theta)
plt.xlabel('time')
plt.ylabel('Theta')
plt.show()


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

ax.plot(t,theta, omega)
ax.set_title("solve_ivp")



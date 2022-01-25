#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 15:13:16 2022

@author: jessielyons
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
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
def f_func(time,state):
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


t_span = (0.0, tf)
X_solve_ivp = solve_ivp(f_func, t_span, X0, t_eval = t)

y = X_solve_ivp.y

print(y.shape)

plt.figure(1)
plt.clf()

plt.plot(X_solve_ivp.t,X_solve_ivp.y[0,:])
plt.xlabel('time')
plt.ylabel('Theta')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

ax.plot(X_solve_ivp.t,
        X_solve_ivp.y[0, :],
        X_solve_ivp.y[1, :])
ax.set_title("solve_ivp")






















#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 08:22:52 2022

@author: jessielyons
"""

from pylab import *
import scipy.constants as pc
import math


## Set initial conditions
#m = float(input("Mass of pendulum object: "))
m=3

#th0 = float(input("Starting position for pendulum in degrees: "))
th0 = 10
th0 = th0 * pi/180.	# Convert starting angle to radians
om0 = 0.0
l = 10.				# Length of pendulum in m

T_est = 2*pi*sqrt(l/pc.g)
print("Estimated period is %g s " % T_est)

#N_period = float(input("Approximate number of periods to plot: "))
N_period = 5
t_max = N_period * T_est

tau = float(input("Size of the time step (s): "))

## Solve ODE using Euler's method

th_old = th0	# Set the initial values of angular displacement, angular
                # velocity, and t (time).
om = om0
t = 0.0

th_plot = array([th_old]) # Make arrays to record the th, om, and t for plotting
om_plot = array([om])
t_plot = array([t])

e0 = 0.5*m*(l**2)*(om0**2) + m*pc.g*l*(1-math.cos(th0))
energy_plot = array([e0])

while (t < t_max):
    #th = th_old + om * tau					# first Euler step
    #om = om - pc.g/l * sin(th) * tau	# second Euler step -----------------------------------------
    
    om = om - pc.g/l * sin(th_old) * tau	# first Euler-Cromer step
    th = th_old + om * tau                 # second Euler-Cromer step
    
    energy = 0.5*m*(l**2)*(om**2) + m*pc.g*l*(1-math.cos(th))
    th_old = th	# set the angle for the next iteration
    t = t + tau	# increase the time by one time step
    
    th_plot = append(th_plot,th)	# append this step's result to the plotting
    om_plot = append(om_plot,om)
    t_plot = append(t_plot,t)
    energy_plot = append(energy_plot, energy)


th_plot = th_plot*180./pi	# Convert angle back to degrees

## Plot the results
figure(1)
clf()
plot(t_plot,th_plot,'r+')
plot(t_plot, energy_plot)
xlabel('time (seconds)')
ylabel(r'$\theta$ (degrees)')
show()
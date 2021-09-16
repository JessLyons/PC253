#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 12:25:27 2021

@author: loaner

The file Mauna.npy contains the CO2 concentration in 
parts per million (ppm) as measured in Manua Loa, Hawaii. The data were 
taken every 14 days, starting in 1981. For simplicity, assume that the 
first measurement was taken January 1st and that every year has 365 days. 

To load the data, save the file in the same directory as your script and use 
numpy.load() as follows:

CO2_ppm_MaunaLoa = np.load("Mauna.npy")

The array of data will then be stored in the variable name CO2_ppm_MaunaLoa.  
You can call your data array whatever you like, but I prefer to use 
something that describes what's in the array.  You'll need to construct an 
array of time points as your x variable.

Fit a straight line to the data to find the average increase in CO2 in 
ppm per year. Plot the data and the fit on the same plot. Don't forget to 
title and label the axes. You could include the average increase in CO2 
in the title of the plot or put it in some of the whitespace by using a 
function we haven't yet seen: plt.text(). 
"""


import matplotlib.pyplot as plt
import numpy as np


co2_conc = np.load('/Users/loaner/Downloads/Mauna_CO2.npy')
days = np.linspace(0,3206,230)

plt.plot(days,co2_conc)

(m,b) = np.polyfit(days, co2_conc, 1)
fit = (m*days) + b

plt.plot(days,fit)

plt.text(x = 0, y = 355, s = 'Average Increase = ' + str(m) + 'ppm')

plt.title('CO2 concentration Average Increase')
plt.xlabel('Time in Years')
plt.ylabel('CO2 Concentration (ppm)')

i = 0
curr_year = 1981
years = []
ticks = []
while i < 3206:
    years.append(curr_year)
    ticks.append(i)
    curr_year = curr_year + 1
    i = i + 365
plt.xticks(ticks = ticks, labels = years)

plt.show()






















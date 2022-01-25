#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 09:22:39 2022

@author: jessielyons
"""

#import the right axis class to give us the 3D option
from mpl_toolkits.mplot3d import Axes3D
import h5py
import numpy as np
import matplotlib.pyplot as plt

filename = "test_ssx_particle_trajectory.h5"


with h5py.File(filename, "r") as f:
    # List all groups
    print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[0]
    
    pos_vec = np.array(f['r'])

    # Get the data
    data = list(f[a_group_key])

xarray = list(pos_vec[:,0])

yarray = list(pos_vec[:,1])

zarray = list(pos_vec[:,2])


print(pos_vec.shape)
#create a 3D axis object
ax = plt.gcf().add_subplot(111, projection='3d')
#make a plot of a trajectory given x, y, and z arrays as a function of time
ax.plot(xarray, yarray, zarray, )

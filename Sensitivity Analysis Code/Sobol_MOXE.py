#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 08:12:23 2021

@author: work
"""
from SALib.sample import saltelli
from SALib.analyze import sobol
from SALib.test_functions import Ishigami
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace, zeros, exp
from MOXE import moxe_function
import math
import os


# problem = {
#     'num_vars': 3,
#     'names': ['x1', 'x2', 'x3'],
#     'bounds': [[-3.14159265359, 3.14159265359],
#                [-3.14159265359, 3.14159265359],
#                [-3.14159265359, 3.14159265359]]
# }

problem = {
    'num_vars': 4,
    'names': ['d', 'delta', 'Sa_Vg', 'tc'],
    'bounds': [[3.7e-6,15.7e-6],
                [0.7e-6,1.3e-6],
                [160,260],
                [1.0,1.6]]
}

param_values = saltelli.sample(problem, 1000)

# x = linspace(0,100,len(param_values))

# plt.scatter(x, param_values)

d = 9.7e-6 # septal wall thickness micrometers 

delta = 1.0e-6 # Alveor-capillary barrier micrometers

Sa_Vg = 210  # Surface area /volume of gas

T = 0.030 # time constant

tc = 1.3# Capillary transit time

# Y = np.zeros([param_values.shape[0]])

# N = len(param_values)

SWT_A = []
Delta_A = []
SVR_A = []
TC_A = []

# for i in range(0,99):
val = 12
N = 100
Y1A = []
Y2A = []
Y3A = []
Y4A = []
for i in range(0,N):
    Y1 = moxe_function(param_values[:,0][i], delta, Sa_Vg, tc, val)
    Y1A.append(Y1)
    
    
for i in range(0,N):
    Y2 = moxe_function(d, param_values[:,1][i], Sa_Vg, tc, val)    
    Y2A.append(Y2)

for i in range(0,N):
    Y3 = moxe_function(d, delta, param_values[:,2][i], tc, val)        
    Y3A.append(Y3)


for i in range(0,N):
    Y4 = moxe_function(d, delta, Sa_Vg, param_values[:,3][i],val) 
    Y4A.append(Y4)

Y = np.vstack((Y1A, Y2A, Y3A, Y4A))
   
Yf = Y.flatten()


Si = sobol.analyze(problem, Yf)
SWT = Si['ST'][0]
SWT_A.append(SWT)

Delta = Si['ST'][1]
Delta_A.append(Delta)

SVR = Si['ST'][2]
SVR_A.append(SVR)

TC = Si['ST'][3]
TC_A.append(SVR)
    
    
# Y = Ishigami.evaluate(param_values)


parameters = ['d', 'delta', 'SVR', 'tc']
PercChangeTP = [Si['S1'][0], Si['S1'][1], Si['S1'][2], Si['S1'][3]]

x = np.arange(len(parameters))  # the label locations
width = 0.35  # the width of the bars

fig4, ax = plt.subplots()

rects1 = ax.bar(x - width/2, PercChangeTP, width, label='TP' , color = 'b',)

ax.set_ylabel('Sobol index, Si')
ax.set_title('100ms')
ax.set_xticks(x)
ax.set_xticklabels(parameters)
# ax.set_ylim([-2,2])
ax.legend()

fig4.tight_layout()

plt.show()

parameters = ['d', 'delta', 'SVR', 'tc']
PercChangeTP = [Si['ST'][0], Si['ST'][1], Si['ST'][2], Si['ST'][3]]

x = np.arange(len(parameters))  # the label locations
width = 0.35  # the width of the bars

fig5, ax = plt.subplots()

rects1 = ax.bar(x - width/2, PercChangeTP, width, label='TP' , color = 'b',)

ax.set_ylabel('Sobol index, St')
ax.set_title('100ms')
ax.set_xticks(x)
ax.set_xticklabels(parameters)
ax.legend()

fig5.tight_layout()

plt.show()

# plt.plot(t[0:99],SWT_A)
# plt.plot(t[0:99],Delta_A)
# plt.plot(t[0:99],SVR_A)
# plt.plot(t[0:99],TC_A)

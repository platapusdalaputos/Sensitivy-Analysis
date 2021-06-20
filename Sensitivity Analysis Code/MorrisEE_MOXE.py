# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Wed Jun 16 16:04:55 2021

# @author: work
# """

# from SALib.sample import saltelli
# from SALib.analyze import morris
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import numpy as np
# from numpy import linspace, zeros, exp
# from MOXE import moxe_function
# import math
# import os


# # problem = {
# #     'num_vars': 3,
# #     'names': ['x1', 'x2', 'x3'],
# #     'bounds': [[-3.14159265359, 3.14159265359],
# #                [-3.14159265359, 3.14159265359],
# #                [-3.14159265359, 3.14159265359]]
# # }



# # x = linspace(0,100,len(param_values))

# # plt.scatter(x, param_values)

# d = 9.7e-6 # septal wall thickness micrometers 

# delta = 1.0e-6 # Alveor-capillary barrier micrometers

# Sa_Vg = 210  # Surface area /volume of gas

# T = 0.030 # time constant

# tc = 1.3# Capillary transit time

# # Y = np.zeros([param_values.shape[0]])

# # N = len(param_values)

# SWT_A = []
# Delta_A = []
# SVR_A = []
# TC_A = []

# for i in range(0,99):
#     val = i
#     N = 10
#     Y1A = []
#     Y2A = []
#     Y3A = []
#     Y4A = []
#     for i in range(0,N):
#         Y1 = moxe_function(param_values[:,0][i], delta, Sa_Vg, tc, val)
#         Y1A.append(Y1)
        
        
#     for i in range(0,N):
#         Y2 = moxe_function(d, param_values[:,1][i], Sa_Vg, tc, val)    
#         Y2A.append(Y2)
    
#     for i in range(0,N):
#         Y3 = moxe_function(d, delta, param_values[:,2][i], tc, val)        
#         Y3A.append(Y3)
    
    
#     for i in range(0,N):
#         Y4 = moxe_function(d, delta, Sa_Vg, param_values[:,3][i],val) 
#         Y4A.append(Y4)
    
#     Y = np.vstack((Y1A, Y2A, Y3A, Y4A))
       
#     Yf = Y.flatten()
    
    
#     Si = morris.analyze(problem, Yf)
#     SWT = Si['ST'][0]
#     SWT_A.append(SWT)
    
#     Delta = Si['ST'][1]
#     Delta_A.append(Delta)
    
#     SVR = Si['ST'][2]
#     SVR_A.append(SVR)
    
#     TC = Si['ST'][3]
#     TC_A.append(SVR)
    
    
# # Y = Ishigami.evaluate(param_values)


# # parameters = ['d', 'delta', 'SVR', 'tc']
# # PercChangeTP = [Si['S1'][0], Si['S1'][1], Si['S1'][2], Si['S1'][3]]

# # x = np.arange(len(parameters))  # the label locations
# # width = 0.35  # the width of the bars

# # fig4, ax = plt.subplots()

# # rects1 = ax.bar(x - width/2, PercChangeTP, width, label='TP' , color = 'b',)

# # ax.set_ylabel('Signal % Change')
# # ax.set_title('100ms')
# # ax.set_xticks(x)
# # ax.set_xticklabels(parameters)
# # ax.set_ylim([-2,2])
# # ax.legend()

# # fig4.tight_layout()

# # plt.show()

# plt.plot(t[0:99],SWT_A)
# plt.plot(t[0:99],Delta_A)
# plt.plot(t[0:99],SVR_A)
# plt.plot(t[0:99],TC_A)

import sys
from SALib.sample.morris import morris
from SALib.util import read_param_file
from SALib.plotting.morris import horizontal_bar_plot, covariance_plot,sample_histograms
from numpy import linspace, zeros, exp
from MOXE import moxe_function
import math
import os
import numpy as np
import matplotlib.pyplot as plt

d = 9.7e-6 # septal wall thickness micrometers 

delta = 1.0e-6 # Alveor-capillary barrier micrometers

Sa_Vg = 210  # Surface area /volume of gas

T = 0.030 # time constant

tc = 1.3# Capillary transit time


problem = {
    'num_vars': 4,
    'names': ['d', 'delta', 'Sa_Vg', 'tc'],
    'bounds': [[3.7e-6,15.7e-6],
                [0.7e-6,1.3e-6],
                [160,260],
                [1.0,1.6]]
}

param_values = morris.sample(problem, 1000, num_levels = 4)

val = 12
N = 1250
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
    
from SALib.analyze import morris

# Perform the sensitivity analysis using the model output
# Specify which column of the output file to analyze (zero-indexed)
Si = morris.analyze(problem, param_values, Yf, conf_level=0.95,
                    print_to_console=True,
                    num_levels=4, num_resamples=100)
# Returns a dictionary with keys 'mu', 'mu_star', 'sigma', and 'mu_star_conf'
# e.g. Si['mu_star'] contains the mu* value for each parameter, in the
# same order as the parameter file

fig, (ax1, ax2) = plt.subplots(1, 2)
horizontal_bar_plot(ax1, Si, {}, sortby='mu_star', unit=r"tCO$_2$/year")
covariance_plot(ax2, Si, {}, unit=r"tCO$_2$/year")

fig2 = plt.figure()
sample_histograms(fig2, param_values, problem, {'color': 'y'})
plt.show()


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 06:02:58 2021

@author: Yohn Taylor
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace, zeros, exp
from MOXE_Code import moxe_function
import math


d = 9.7e-6 # septal wall thickness micrometers 

delta = 1.0e-6 # Alveor-capillary barrier micrometers

Lambda_tiss = 0.1 # Ostwald solubility of xenon in lung septum (In vivo methods and applications of xenon-129 magnetic resonance)
Lambda_tiss1 = 0.1 # Ostwald solubility of xenon in lung septum (In vivo methods and applications of xenon-129 magnetic resonance)

Sa_Vg = 210  # Surface area /volume of gas
Sa_Vg1 = 210  # Surface area /volume of gas

T = 0.030 # time constant
tc = 1.3 # Capillary transit time

'''The healthy range values for the physiological parameters'''
M = 100;

Sa_VgLim = np.linspace(160,260,M)
dLim = np.linspace(3.7e-6,15.7e-6,M)
deltaLim = np.linspace(0.7e-6,1.3e-6,M)
TLim = np.linspace(0.020,0.039,M)
HCTConstant = np.linspace(23,31,M)
txConstant = np.linspace(1.0,1.6,M)   

sigTP1, sigRBC1, t = moxe_function(d, delta, Lambda_tiss, Sa_Vg, tc, T)


''' Sensitivity of the Blood-air barrier thickness '''

TP = []
RBC = []
labels = ['Lowest', 'Lowest1', 'lowest2', 'lowest3', 'mid', 'upper3', 'upper2', 'upper1', 'upper']


for i in range(len(dLim)):  

    sigTP, sigRBC, t = moxe_function(d, delta, Lambda_tiss, Sa_Vg, tc, TLim[i])
    TP.append(sigTP)
    RBC.append(sigRBC)
 
''' Plotting the Tissue Phase '''

N = M # iterations for the cmap
cmap = plt.get_cmap('jet',N)

fig = plt.figure(figsize=(8,6))
ax1 = fig.add_axes([0.10,0.10,0.70,0.85])
ax2 = fig.add_axes([0.10,0.10,0.70,0.85])

for i  in range(N):
    ax1.plot(t,TP[i],c=cmap(i))   

plt.ylabel('Signal Amplitude a.u.')
plt.xlabel('Delay/Exchange Time (s)')
plt.title('TP')
norm = mpl.colors.Normalize(vmin=0,vmax=2)
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
plt.colorbar(sm, boundaries=np.arange(-0.05,2.1,.1))
plt.show()


''' Plotting the RBC Phase '''

N = M
cmap = plt.get_cmap('jet',N)

fig = plt.figure(figsize=(8,6))
ax2 = fig.add_axes([0.10,0.10,0.70,0.85])

for i  in range(N):
    ax2.plot(t,RBC[i],c=cmap(i))   

plt.ylabel('Signal Amplitude a.u.')
plt.xlabel('Delay/Exchange Time (s)')
plt.title('RBC')

norm = mpl.colors.Normalize(vmin=0,vmax=2)
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
plt.colorbar(sm, boundaries=np.arange(-0.05,2.1,.1))
plt.show()


''' Calculating the percentage signal change for the different Parameters '''

''' TP '''

ax3 = fig.add_axes([0.10,0.10,0.70,0.85])

for i in range(N):
    P = ((TP[i]/sigTP1)-1)*100
    plt.plot(t, P, c=cmap(i))

plt.ylabel('Signal Amplitude a.u.')
plt.xlabel('Delay/Exchange Time (s)')
plt.title('TP')

norm = mpl.colors.Normalize(vmin=0,vmax=2)
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
plt.colorbar(sm, boundaries=np.arange(-0.05,2.1,.1))
plt.show()

''' RBC '''

ax4 = fig.add_axes([0.10,0.10,0.70,0.85])

for i in range(N):
    P = ((RBC[i]/sigRBC1)-1)*100
    plt.plot(t, P, c=cmap(i))

plt.ylabel('Signal Amplitude a.u.')
plt.xlabel('Delay/Exchange Time (s)')
plt.title('RBC')

norm = mpl.colors.Normalize(vmin=0,vmax=2)
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
plt.colorbar(sm, boundaries=np.arange(-0.05,2.1,.1))
plt.show()

# for i in range(len(dLim)):
#     fTP = plt.figure(1)
#     # plt.plot(t,TP[i], label = labels[i])
#     plt.plot(t,TP[i])
#     plt.xlabel('Delay Time (s)')
#     plt.ylabel('Signal Amplitude a.u.')
#     plt.title('Tissue Phase (TP) blood???air barrier')
#     # plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),fancybox=True, shadow=True, ncol=5)
    
#     fRBC = plt.figure(2)
#     # plt.plot(t,RBC[i], label = labels[i])
#     plt.plot(t,RBC[i])
#     plt.xlabel('Delay Time (s)')
#     plt.ylabel('Signal Amplitude a.u.')
#     plt.title('RBC Phase (RBC) blood???air barrier')    
#     # plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),fancybox=True, shadow=True, ncol=5)

# ''' Calculating the percentage change for the different Parameters '''

# percCh_TP = []
# percCh_RBC = []
# for i in range(len(dLim)):
    
#     percTP = ((TP[i]/sigTP1)-1)*100
#     percTP = [0 if math.isnan(x) else x for x in percTP]
#     percCh_TP.append(percTP)
    
#     percRBC = ((RBC[i]/sigRBC1)-1)*100
#     percRBC = [0 if math.isnan(x) else x for x in percRBC]
#     percCh_RBC.append(percRBC)
    
#     # percTP = ((TP[i]/sigTP1) - 1)*100
#     # percCh_TP.append(percTP)
#     # percRBC = ((RBC[i]/sigRBC1) - 1)*100
#     # percCh_RBC.append(percRBC)
#     # plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),fancybox=True, shadow=True, ncol=5)

# for i in range(len(dLim)):
#     fTP2 = plt.figure(3)
#     # plt.plot(t,percCh_TP[i], label = labels[i])
#     plt.plot(t,percCh_TP[i])
#     plt.xlabel('Delay Time (s)')
#     plt.ylabel('Signal % increase')
#     plt.title('SA blood???air barrier thickness TP')
#     # plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),fancybox=True, shadow=True, ncol=5)
#     # plt.legend()
#     # plt.savefig('SA blood???air barrier thickness TP.png')

#     fRBC2 = plt.figure(4)
#     # plt.plot(t,percCh_RBC[i], label = labels[i])
#     plt.plot(t,percCh_RBC[i])
#     plt.xlabel('Delay Time (s)')
#     plt.ylabel('Signal % increase')
#     plt.title('SA blood???air barrier thickness RBC')
#     # plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),fancybox=True, shadow=True, ncol=5)
 
# ''' plotting individual upper and lower limits '''
# Fig = plt.figure(5)
# # plt.plot(t,percCh_TP[0], label = 'lowest')
# plt.plot(t,percCh_TP[0])
# plt.xlabel('Delay Time (s)')
# plt.ylabel('Signal % increase')
# plt.title('SA blood???air barrier thickness TP')
# plt.legend()

# Fig = plt.figure(6)
# plt.plot(t,percCh_TP[8], label = 'upper')
# plt.xlabel('Delay Time (s)')
# plt.ylabel('Signal % increase')
# plt.title('SA blood???air barrier thickness TP')
# plt.legend()

# Fig = plt.figure(7)
# plt.plot(t,percCh_RBC[0], label = 'lowest')
# plt.xlabel('Delay Time (s)')
# plt.ylabel('Signal % increase')
# plt.title('SA blood???air barrier thickness RBC')
# plt.legend()

# Fig = plt.figure(8)
# plt.plot(t,percCh_RBC[8], label = 'upper')
# plt.xlabel('Delay Time (s)')
# plt.ylabel('Signal % increase')
# plt.title('SA blood???air barrier thickness RBC')
# plt.legend()


# res1 = [i / j for i, j in zip(signal1, signal2)]
# res2 = [i / j for i, j in zip(signal1, signal3)]
# res3 = [i / j for i, j in zip(signal1, signal4)]
# res4 = [i / j for i, j in zip(signal1, signal5)]





    
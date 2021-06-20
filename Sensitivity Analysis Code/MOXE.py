#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 12:07:29 2021

@author: work
"""
import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace, zeros, exp
import math

#Parameters for the uptake curves

# Lamda =  # Ostwald solubility

# d =      # Septal thickness tissue + capillary + tissue

# D =      # Diffusion coefficient

# delta =  # tissue thickness

# Sa =     # Surface area in the lungs

# Vg =     # volume of the gas

def moxe_function(d, delta, Sa_VgLim, tcLim, val):

    k = delta/d  # delta/d     # tissue thickness/septal thickness
    
    T =  0.030 # s for seconds (d**2/(pi**2)*D) # Uptake time constant
    
    Lambda_tiss = 0.1
    
    mu = 100*Lambda_tiss*d*Sa_VgLim #((Lamda*d*Sa)/Vg) 
    
    eta = 0.5 # greek n
    
    
    tc = tcLim # s for seconds
    
    
    t = np.linspace(0.01,0.8,100) # s for seconds
    # print(t)
    N = 9
    ''' Attaining the values for the slope for Sd1(t)'''
    
    Sd1_append = []
    fourth_val =[]
    
    for ii in range(0,len(t)):
        #Appends the list of appended A into a nested list
        B=[]
        for n in range(1, N):
            if(n % 2 != 0):
                s=[]
                A = (1/n**2)*(1-np.cos(n*np.pi*k))*exp(((-n**2)*t[ii])/T)
                s.append(A)
                if s not in B:
                    B.append(s)
                    #extracts and sums the lists within a list
                    res = list() 
                    for j in range(0, len(B[0])): 
                        tmp = 0
                        for i in range(0, len(B)):
                            
                            tmp = tmp + B[i][j] 
                            
                        res.append(tmp) 
        #Turns the list into a np.array
        Gres = np.array(res)
    
        Sd1 =mu*(2*k - ((8/np.pi**2)*Gres))
        Sd1_append.append(Sd1)
    
    ''' Attaining the values for the slope for Sd2s(t)'''

    Sd2s_append = []
    
    for ii in range(len(t)): # t is time in ms
        B1 = []
        for n in range(1, N):
            if(n % 2 != 0):
                s1=[]
                A1 = (1/n**2)*(np.cos(n*np.pi*k))*exp(((-n**2)*t[ii])/T)
                s1.append(A1)
                if s1 not in B1:
                    B1.append(s1)
                    #extracts and sums the lists within a list
                    res_1 = list() 
                    for j in range(0, len(B1[0])): 
                        tmp_1 = 0
                        for i in range(0, len(B1)):
                            
                            tmp_1 = tmp_1 + B1[i][j] 
                            
                        res_1.append(tmp_1) 
                        
        Gres_1 = np.array(res_1)
    
        Sd2s = (mu*((1-2*k) - ((8/np.pi**2))*Gres_1))
        Sd2s_append.append(Sd2s)
    
    ''' Sd2 part1  '''
    
    Sd2_append = []
    
    for ii in range(len(t)): # t is time in ms
        B2 = []
        for n in range(1, N):
            if(n % 2 != 0):
                s2=[]
                A2 = (1/n**4)*(np.cos(n*np.pi*k))*(1-exp(((-n**2)*t[ii])/T))
                s2.append(A2)
                if s2 not in B2:
                    B2.append(s2)
                    #extracts and sums the lists within a list
                    res_2 = list() 
                    for e in range(0, len(B2[0])): 
                        tmp_2 = 0
                        for f in range(0, len(B2)):
                            
                            tmp_2 = tmp_2 + B2[f][e] 
                            
                        res_2.append(tmp_2) 
                        
        Gres_2 = np.array(res_2)
    
        Sd2 = 2*mu*(((1-(2*k))*(t[ii]/tc)) - ((8/(np.pi**2))*(T/tc))*Gres_2)
        Sd2_append.append(Sd2)
    
    ''' Sd2 part2  '''
    
    Sd22_append = []
    
    for ii in range(len(t)): # t is time in ms
        B3 = []
        for n in range(1, N):
            if(n % 2 != 0):
                s3=[]
                A3 = (1/n**2)*(np.cos(n*np.pi*k))*exp(((-n**2)*t[ii])/T)
                s3.append(A3)
                if s3 not in B3:
                    B3.append(s3)
                    #extracts and sums the lists within a list
                    res_3 = list() 
                    for e in range(0, len(B3[0])): 
                        tmp_3 = 0
                        for f in range(0, len(B3)):
                            
                            tmp_3 = tmp_3 + B3[f][e] 
                            
                        res_3.append(tmp_3) 
                        
        Gres_3 = np.array(res_3)
    
        Sd22 = mu*(1-(t[ii]/tc))*((((1-(2*k))) - ((8/(np.pi**2))*Gres_3)))
        Sd22_append.append(Sd22)
    
    
    
    Sd1np = np.array(Sd1_append)
    Sd2np = np.array(Sd2_append)
    Sd22np = np.array(Sd22_append)
    S_d2 = (Sd22np + Sd2np)
    
    ''' putting it all together '''
    
    Srbc = eta*S_d2
    Stp = Sd1np + (1-eta)*S_d2
    
    Stp = Stp.flatten()
    Srbc = Srbc.flatten()
    # Stp = np.hstack((0,Stp))
    # Srbc = np.hstack((0,Srbc))
    # t = np.linspace(0.0,0.8,len(Stp)) # s for seconds  
    
    return Srbc[val]


# plt.plot(t,Stp,'r',label = 'Tissue Phase')
# plt.plot(t,Srbc,'b',label = 'RBC Phase')
# plt.title('MOXE Simulation')
# plt.xlabel('Delay Time (s)')
# plt.ylabel('Signal Amplitude (a.u)')
# plt.legend()
# plt.show()

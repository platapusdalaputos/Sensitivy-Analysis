#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 14:32:53 2021

@author: work
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 22:16:25 2021

@author: work

"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace, zeros, exp
from MOXE_Code import moxe_function
import math



def SigIncrease_delta():    
    
    
    ''' This function calculates the values for the upper and lower limit parameter values '''
    
    d = 9.7e-6 # septal wall thickness micrometers 
    
    delta = 1.0e-6 # Alveor-capillary barrier micrometers
    
    Lambda_tiss = 0.1 # Ostwald solubility of xenon in lung septum (In vivo methods and applications of xenon-129 magnetic resonance)
    
    Sa_Vg = 210  # Surface area /volume of gas
    
    T = 0.030 # time constant
    
    tc = 1.3# Capillary transit time
    
    '''The healthy range values ABOVE THE MEAN for the physiological parameters'''
    
    sigTP1, sigRBC1, t = moxe_function(d, delta, Lambda_tiss, Sa_Vg, tc, T)
    plt.plot(t, sigTP1, 'b')
    plt.plot(t, sigRBC1, 'r')

    
    Sa_VgLim = [160, 260]
    dLim = [3.7e-6,15.7e-6]
    deltaLim = [0.7e-6,1.3e-6]
    TLim = [0.020,0.039]
    HCTConstant = [23,31]
    txConstant = [1.3,1.6]
    
    ''' Calculating Sensitivity  '''
    
    TP = []
    RBC = []
    labels = ['Lowest', 'Lowest1', 'lowest2', 'lowest3', 'mid', 'upper3', 'upper2', 'upper1', 'upper']
    
    
    for i in range(len(dLim)):  
    
        sigTP, sigRBC, t = moxe_function(d, deltaLim[i], Lambda_tiss, Sa_Vg, tc, T)
        TP.append(sigTP)
        RBC.append(sigRBC)
      
    
    ''' Calculating the percentage signal change for the different Parameters '''
    
    ''' TP '''
    Ptp = []    
    Prbc =[]
    
    N = len(deltaLim)
    
    for i in range(N):
        P1 = ((TP[i]/sigTP1)-1)*100
        Ptp.append(P1)

    
    ''' RBC '''
        
    for i in range(N):
        P2 = ((RBC[i]/sigRBC1)-1)*100
        Prbc.append(P2)
        
    return(TP, RBC, Ptp, Prbc, t)
    
def SigIncreaseSVR():    
    
    
    ''' This function calculates the values for the upper and lower limit parameter values '''
    
    d = 9.7e-6 # septal wall thickness micrometers 
    
    delta = 1.0e-6 # Alveor-capillary barrier micrometers
    
    Lambda_tiss = 0.1 # Ostwald solubility of xenon in lung septum (In vivo methods and applications of xenon-129 magnetic resonance)
    
    Sa_Vg = 210  # Surface area /volume of gas
    
    T = 0.030 # time constant
    
    tc = 1.3# Capillary transit time
    
    '''The healthy range values ABOVE THE MEAN for the physiological parameters'''
    
    sigTP1, sigRBC1, t = moxe_function(d, delta, Lambda_tiss, Sa_Vg, tc, T)
    plt.plot(t, sigTP1, 'b')
    plt.plot(t, sigRBC1, 'r')

    
    Sa_VgLim = [160, 260]
    dLim = [3.7e-6,15.7e-6]
    deltaLim = [0.7e-6,1.3e-6]
    TLim = [0.020,0.039]
    HCTConstant = [23,31]
    txConstant = [1.3,1.6]
    
    ''' Calculating Sensitivity  '''
    
    TP = []
    RBC = []
    labels = ['Lowest', 'Lowest1', 'lowest2', 'lowest3', 'mid', 'upper3', 'upper2', 'upper1', 'upper']
    
    
    for i in range(len(dLim)):  
    
        sigTP, sigRBC, t = moxe_function(d, delta, Lambda_tiss, Sa_VgLim[i], tc, T)
        TP.append(sigTP)
        RBC.append(sigRBC)
      
    
    ''' Calculating the percentage signal change for the different Parameters '''
    
    ''' TP '''
    Ptp = []    
    Prbc =[]
    
    N = len(Sa_VgLim)

    
    for i in range(N):
        P1 = ((TP[i]/sigTP1)-1)*100
        Ptp.append(P1)

    
    ''' RBC '''
        
    for i in range(N):
        P2 = ((RBC[i]/sigRBC1)-1)*100
        Prbc.append(P2)
        
    return(TP, RBC, Ptp, Prbc)



def SigIncreaseTx():    
    
    
    ''' This function calculates the values for the upper and lower limit parameter values '''
    
    d = 9.7e-6 # septal wall thickness micrometers 
    
    delta = 1.0e-6 # Alveor-capillary barrier micrometers
    
    Lambda_tiss = 0.1 # Ostwald solubility of xenon in lung septum (In vivo methods and applications of xenon-129 magnetic resonance)
    
    Sa_Vg = 210  # Surface area /volume of gas
    
    T = 0.030 # time constant
    
    tc = 1.3# Capillary transit time
    
    '''The healthy range values ABOVE THE MEAN for the physiological parameters'''
    
    sigTP1, sigRBC1, t = moxe_function(d, delta, Lambda_tiss, Sa_Vg, tc, T)
    plt.plot(t, sigTP1, 'b')
    plt.plot(t, sigRBC1, 'r')

    
    Sa_VgLim = [160, 260]
    dLim = [3.7e-6,15.7e-6]
    deltaLim = [0.7e-6,1.3e-6]
    TLim = [0.020,0.039]
    HCTConstant = [23,31]
    txConstant = [1.0,1.6]
    
    ''' Calculating Sensitivity  '''
    
    TP = []
    RBC = []
    labels = ['Lowest', 'Lowest1', 'lowest2', 'lowest3', 'mid', 'upper3', 'upper2', 'upper1', 'upper']
    
    
    for i in range(len(dLim)):  
    
        sigTP, sigRBC, t = moxe_function(d, delta, Lambda_tiss, Sa_Vg, txConstant[i], T)
        TP.append(sigTP)
        RBC.append(sigRBC)
      
    
    ''' Calculating the percentage signal change for the different Parameters '''
    
    ''' TP '''
    Ptp = []    
    Prbc =[]
    N = len(txConstant)

    for i in range(N):
        P1 = ((TP[i]/sigTP1)-1)*100
        Ptp.append(P1)

    
    ''' RBC '''
        
    for i in range(N):
        P2 = ((RBC[i]/sigRBC1)-1)*100
        Prbc.append(P2)
        
    return(TP, RBC, Ptp, Prbc)
    
def SigIncrease_d():    
    
    
    ''' This function calculates the values for the upper and lower limit parameter values '''
    
    d = 9.7e-6 # septal wall thickness micrometers 
    
    delta = 1.0e-6 # Alveor-capillary barrier micrometers
    
    Lambda_tiss = 0.1 # Ostwald solubility of xenon in lung septum (In vivo methods and applications of xenon-129 magnetic resonance)
    
    Sa_Vg = 210  # Surface area /volume of gas
    
    T = 0.030 # time constant
    
    tc = 1.3# Capillary transit time
    
    '''The healthy range values ABOVE THE MEAN for the physiological parameters'''
    
    sigTP1, sigRBC1, t = moxe_function(d, delta, Lambda_tiss, Sa_Vg, tc, T)
    plt.plot(t, sigTP1, 'b')
    plt.plot(t, sigRBC1, 'r')

    
    Sa_VgLim = [160, 260]
    dLim = [3.7e-6,15.7e-6]
    deltaLim = [0.7e-6,1.3e-6]
    TLim = [0.020,0.039]
    HCTConstant = [23,31]
    txConstant = [1.3,1.6]
    
    ''' Calculating Sensitivity  '''
    
    TP = []
    RBC = []
    labels = ['Lowest', 'Lowest1', 'lowest2', 'lowest3', 'mid', 'upper3', 'upper2', 'upper1', 'upper']
    
    
    for i in range(len(dLim)):  
    
        sigTP, sigRBC, t = moxe_function(dLim[i], delta, Lambda_tiss, Sa_Vg, tc, T)
        TP.append(sigTP)
        RBC.append(sigRBC)
      
    
    ''' Calculating the percentage signal change for the different Parameters '''
    
    ''' TP '''
    Ptp = []    
    Prbc =[]
    
    N = len(dLim)

    
    for i in range(N):
        P1 = ((TP[i]/sigTP1)-1)*100
        Ptp.append(P1)

    
    ''' RBC '''
        
    for i in range(N):
        P2 = ((RBC[i]/sigRBC1)-1)*100
        Prbc.append(P2)
        
    return(TP, RBC, Ptp, Prbc)
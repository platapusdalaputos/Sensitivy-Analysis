import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace, zeros, exp
from MOXE_sensitivity_analysis import moxe_tp_function
import math

A = [0.9, 0.8, 0.7, 0.6] # percentage change

d = 10e-6 # micrometers 

d1= 10e-6

delta = 1.5e-6 # micrometers
delta1 = 1.5e-6 # micrometers

Lambda_tiss = 0.1 # Ostwald solubility of xenon in lung septum (In vivo methods and applications of xenon-129 magnetic resonance)
Lambda_tiss1 = 0.1 # Ostwald solubility of xenon in lung septum (In vivo methods and applications of xenon-129 magnetic resonance)

Sa_Vg = 30000  # Surface area /volume of gas
Sa_Vg1 = 30000  # Surface area /volume of gas


# for i in range(1,50):
   

signal1, signal12 = moxe_tp_function(d, delta, Lambda_tiss, Sa_Vg)

print(signal1)

# # signal2 = moxe_tp_function(d1*A, delta1, Lambda_tiss1, Sa_Vg1)
# # signal3 = moxe_tp_function(d1, delta1*A, Lambda_tiss1, Sa_Vg1)
# # signal4 = moxe_tp_function(d1, delta1, Lambda_tiss1*A, Sa_Vg1)
# # signal5 = moxe_tp_function(d1, delta1, Lambda_tiss1, Sa_Vg1*A)



# for i in range(1,4):
# if i == 1:
signal2 = moxe_tp_function(d1*0.9, delta1, Lambda_tiss1, Sa_Vg1)
# elif i==2:
signal3 = moxe_tp_function(d1*0.8, delta1, Lambda_tiss1, Sa_Vg1)
# elif i==3:
signal4 = moxe_tp_function(d1*0.7, delta1, Lambda_tiss1, Sa_Vg1)
# elif i==4:
signal5 = moxe_tp_function(d1*0.6, delta1, Lambda_tiss1, Sa_Vg1)
                                   



#     # print(signal2)
#     # print(signal3)
#     # print(signal4)
# print(signal5)
# # plt.plot(signal1, label = 'signal1')
# # plt.plot(signal2, label = 'signal2')
# # plt.xlabel('time(ms)')
# # plt.ylabel('Amplitude')
# # plt.title('')
# # plt.legend()
# # plt.show()



res1 = [i / j for i, j in zip(signal1, signal2)]
res2 = [i / j for i, j in zip(signal1, signal3)]
res3 = [i / j for i, j in zip(signal1, signal4)]
res4 = [i / j for i, j in zip(signal1, signal5)]


for i in range(len(res1)):
    res1[i] = (res1[i] - 1)*100

for i in range(len(res2)):
    res2[i] = (res2[i] - 1)*100

for i in range(len(res3)):
    res3[i] = (res3[i] - 1)*100

for i in range(len(res4)):
    res4[i] = (res4[i] - 1)*100


# Allplots = np.array([res1, res2, res3, res4])
# # newArray = Allplots.reshape(1, 1)
# # Allplots2 = all

# # print(Allplots)
# plt.plot(Allplots[1], label = 'd-10') 
# plt.plot(Allplots[2], label = 'd-20') 

# plt.plot(res2, label = 'd-20')
# plt.plot(res3, label = 'd-30')
# plt.plot(res4, label = 'd-40')
# plt.plot(Allplots)
# plt.xlabel('delay time(ms)')
# plt.ylabel('signal percetange change')
# plt.legend()
# print(res)


# t, x = np.pi*np.mgrid[0:1:100j, 0:1:100j]
# val = x
# new_x = x*np.exp(t)
# # plt.contourf(t, new_x, val)
# plt.pcolormesh(t, new_x, val)
# plt.xlabel("t")
# plt.ylabel("x")
# plt.show()






    
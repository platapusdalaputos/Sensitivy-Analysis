import matplotlib.pyplot as plt
import numpy as np
import math
from numpy import linspace, zeros, exp
from SALib.sample import saltelli
from SALib.analyze import sobol
from SALib.test_functions import Ishigami
# uD = uniform distribution ---> np.random.uniform(low, high, size)

M = 1000 # size of the distribution
uD_Sa_VgLim = np.random.uniform(160, 260, M)
uD_dLim = np.random.uniform(9.7e-6,15.7e-6,M)
UD_deltaLim = np.random.uniform(0.7e-6,1.3e-6,M)
uD_TLim = np.random.uniform(0.020,0.039,M)
uD_HCTConstant = np.random.uniform(23,31,M)
uD_txConstant = np.random.uniform(1.0,1.6,M) 

''' Morris Method Plot'''


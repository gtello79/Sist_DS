import numpy as np
import pandas as pd
from Class.QPSO import Q_PSO

DATA_PATH = "Data/kddtest.txt"
data = pd.read_csv(DATA_PATH)
xe = data.iloc[0:1000, 1:39] #probando sample mas chico
ye = data.iloc[0:1000, 39]
   
N, D = xe.shape
xe = np.array(xe)
ye = np.array(ye)

X0 = np.ones((N,1))
Xe = np.hstack((xe, X0))
    
D += 1
    
PARAM_CONFIG_PATH = "param_config.csv"
params = pd.read_csv(PARAM_CONFIG_PATH)
L = params.iloc[0,0]
C = params.iloc[0,1]
maxIter = params.iloc[0,2]
numPart = params.iloc[0,3]
q = Q_PSO(maxIter, numPart, L, D, Xe, ye, C)
w1, w2, MSE = q.run_QPSO()

np.savez("pesos", w1 = w1, w2 = w2, MSE = MSE)

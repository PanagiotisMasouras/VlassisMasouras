import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# time in seconds
time = [  0,  10,  20,  30,  39,  49,  58,  67,  78,  88, 99,
       109, 119, 129, 140, 154, 170, 180, 190, 200]
# concentrations in g/L
conc = [0, 0.02, 0.15, 0.4, 0.62, 0.71, 0.48, 0.36, 0.25,
        0.19, 0.15, 0.12, 0.1, 0.08, 0.06, 0.04, 0.02, 0.01, 0, 0]

def Trap(time,conc):
    E_tot1=0
    for i in range(len(time) - 1):
        dx1=time[i+1]-time[i]
        dc1=conc[i+1]+conc[i]
        E1=0.5*dx1*dc1
        E_tot1=E_tot1+E1
    return E_tot1
resultT = Trap(time, conc)
print("E_tot_Trap =", resultT)

def LR(time,conc):
    E_tot2=0
    n=len(time)-1
    for i in range(len(conc)-1):
        dx2 = (time[i+1] - time[i])
        dc2=conc[i]
        E2=dx2*dc2
        E_tot2=E_tot2+E2
    return E_tot2
resultLR = LR(time, conc)
print("E_tot_LR =", resultLR)

def RR(time,conc):
    E_tot3=0
    n=len(time)-1
    for i in range(len(conc)-1):
        dx3 = (time[i+1] - time[i])
        dc3=conc[i+1]
        E3=dx3*dc3
        E_tot3=E_tot3+E3
    return E_tot3
resultRR = RR(time, conc)
print("E_tot_RR =", resultRR)

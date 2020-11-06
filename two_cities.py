#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 14:55:07 2020

@author: JORGE TABANERA BRAVO
"""

from numpy import ones

import pylab as py


#### EVOLUTION FUNCTION

def evolution(beta, Gamma21, Gamma12, S10, I10, S20, I20):
    
    # INITIAL CONDITION
    
    S1 = S10
    I1 = I10
    
    S2 = S20
    I2 = I20
    
    # SYSTEM EVOLUTION
    
    s1 = []
    s2 = []
    i1 = []
    i2 = []
    
    for time in range(100):
        
        s1.append(S1)
        s2.append(S2)
        i1.append(I1)
        i2.append(I2)
    
        S1 = S1 - beta*S1*I1 - Gamma21*S1 + Gamma12*S2
        S2 = S2 - beta*S2*I2 - Gamma12*S2 + Gamma21*S1
        
        I1 = I1 + beta*S1*I1 -gamma*I1 - Gamma21*I1 + Gamma12*I2
        I2 = I2 + beta*S2*I2 - gamma*I2 - Gamma12*I2 + Gamma21*I1
        
    return  S1, I1, S2, I2


#### SILENCIO, SE RUEDA

# paramenters of evolution
    
beta = 0.01
gamma = 0.01
Gamma12 = 0.001
Gamma21 = 0.001

s1, i1, s2, i2 = evolution(beta, Gamma21, Gamma12, S10, I10, S20, I20)

py.plot(s2, color = 'r')
py.plot(i2, color = 'r', linestyle = '-.')
    

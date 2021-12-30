# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 13:18:32 2021

@author: 1026313
"""
import numpy as np

W = np.array([[-2,4,-1], [6,0,-3]])
b = np.array([0.1, -2.5])
a = np.array([0.3, 0.4, 0.1])

a_1 = W @ a + b

print(np.tanh(a_1))
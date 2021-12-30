# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:43:45 2021

@author: 1026313
"""
import numpy as np

A = [[1, 1, 1],
     [3, 2, 1],
     [2, 1, 2]]

Ainv = np.linalg.inv(A)

B = [[1, 1, 1],
     [3, 2, 1],
     [2, 1, 2]]

s = [15, 28, 23]

r = np.linalg.solve(A, s)



# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 12:45:22 2021

@author: 1026313
"""
import numpy as np

A = [[4, -5, 6],
     [7, -8, 6],
     [3/2, -1/2, -2]]

A_eVals, A_eigVecs = np.linalg.eig(A)

#######################################################################################
L = [[0, 0, 0, 1],
     [1, 0, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 1, 0]]

L = [[0.1, 0.1, 0.1, 0.7],
     [0.7, 0.1, 0.1, 0.1],
     [0.1, 0.7, 0.1, 0.1],
     [0.1, 0.1, 0.7, 0.1]]

L_eVals, L_eVecs = np.linalg.eig(L)

order = np.absolute(L_eVals).argsort()[::-1] # Orders them by their eigenvalues
L_eVals = L_eVals[order]
L_eVecs = L_eVecs[:,order]

r = L_eVecs[:, 0] # Sets r to be the principal eigenvector
100 * np.real(r / np.sum(r)) # Make this eigenvector sum to one, then multiply by 100 Procrastinating Pats


########################################################################################

L = [[0, 1, 0, 0],
     [1, 0, 0, 0],
     [0, 0, 0, 1],
     [0, 0, 1, 0]]

L = [[0.1, 0.7, 0.1, 0.1],
     [0.7, 0.1, 0.1, 0.1],
     [0.1, 0.1, 0.1, 0.7],
     [0.1, 0.1, 0.7, 0.1]]

L_eVals, L_eVecs = np.linalg.eig(L)

order = np.absolute(L_eVals).argsort()[::-1] # Orders them by their eigenvalues
L_eVals = L_eVals[order]
L_eVecs = L_eVecs[:,order]

r = L_eVecs[:, 0] # Sets r to be the principal eigenvector
100 * np.real(r / np.sum(r))

########################################################################################

M = [[3/2, -1],
     [-1/2, 1/2]]

M_eVals, M_eigVecs = np.linalg.eig(M)

D = np.linalg.inv(M_eigVecs) @ M @ M_eigVecs

M_prime = M_eigVecs @ D @ D @ np.linalg.inv(M_eigVecs)
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:34:34 2020

@author: aubin
"""
# Import of the module numpy for using matrices 
import numpy as np

######################################################################################
####### Coeur du programme, utilisé par la suite pour les 5 autres scénarios #########
######################################################################################

X_MAX = 10
X_CRITICAL = 3
X_MIN = X_CRITICAL + 1
CRIT_MAX_RANGE = list(range(X_CRITICAL, X_MAX))
FORAGE_COST = 1
N_PATCH = 3
HORIZON = 20
p_mortality = [0, 0.004, 0.02]
p_benefit = [1, 0.4, 0.6]
benefit = [0, 3, 5]
rhs = [0] * N_PATCH
# Initialisation of the f_vector matrix that helps making the steps
f_vectors = np.zeros([X_MAX, 2])
f_vectors[CRIT_MAX_RANGE, 1] = 1

fxtt = np.zeros([HORIZON, X_MAX])
mat_best_patch = np.zeros([HORIZON, X_MAX])

TIME = HORIZON - 1

while TIME > 0:
    TIME -= 1
    over_states()
    f_vectors[:, 1] = np.matrix.copy(fxtt[TIME, :])
mat_best_patch[HORIZON - 1, :] = list(range(1, X_MAX+1))
mat_best_patch = mat_best_patch[:, CRIT_MAX_RANGE]

fxtt[HORIZON - 1, : ] = list(range(1,X_MAX+1))
fxtt = fxtt[:, CRIT_MAX_RANGE]

print(mat_best_patch)
with np.printoptions(precision = 3):
    print(fxtt)

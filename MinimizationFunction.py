import numpy as np
from scipy.optimize import minimize

funcs = np.stack((f, f1, f2, f3, f4)) # Stacks the functions
def minimisefunc(x,funcs):
    ''' 
    Data types:
    f: np.array
    f1: np.array
    f2: np.array
    f3: np.array
    f4: np.array

    Define a function to compute f(t) - af1 + bf2 + cf3 + df4 
    and minimising the known funcs to find a solution of values for x = [a, b, c, d]
    '''
    a, b, c, d = x # internal to the function
    diffarray = (
        funcs[0] - 
        (a*funcs[1] + b*funcs[2] + c*funcs[3] + d*funcs[4])
    )
    sumsquares = (diffarray**2).sum() 
    return sumsquares

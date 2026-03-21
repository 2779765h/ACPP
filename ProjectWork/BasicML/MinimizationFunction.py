import numpy as np
from scipy.optimize import minimize

def minimisefunc(x, funcs):
    ''' 
    A function that can be used for optimisation using Scipy minimize. 
    Compute f(t) - (af1 + bf2 + cf3 + df4) and minimise funcs 
    to find a solution of values for x = [a, b, c, d].
    
    Parameters
    ----------
    x: numpy array
        coefficient array x = [a, b, c, d] to be optimised
    funcs: numpy array
        array of stacked functions, i.e.,
        funcs = np.stack((f, f1, f2, f3, f4)) 

    Returns
    ----------
    sumsquares: float
        sum of the squared differences
    '''
    a, b, c, d = x # internal to the function
    diffarray = (
        funcs[0] - 
        (a*funcs[1] + b*funcs[2] + c*funcs[3] + d*funcs[4])
    )
    sumsquares = (diffarray**2).sum() 
    return sumsquares

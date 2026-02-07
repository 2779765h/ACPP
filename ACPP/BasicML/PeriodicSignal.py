import numpy as np

def sinfunc(t, a, b, c, d, t1, t2, t3):
    '''
    Data types:
    t: np.float
    a: float
    b: float
    c: float
    d: float
    t1: np.float
    t2: np.float
    t2: np.float
    return: np.array

    This function calculates a periodic signal f(t) based on the linear combination of functions of the form:
    f(t) = a*sin(t-t1) + bsin(2t-t2) + csin(3t-t3) + 1
    '''
    return (a*np.sin(t - t1)) + (b*np.sin(2*t - t2)) + (c*np.sin(3*t - t3)) + (d*1)

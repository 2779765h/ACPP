import numpy as np

def sinfunc(t, a, b, c, d, t1, t2, t3):
    '''
    This function calculates a periodic signal f(t) based on the linear combination of functions of the form:
    f(t) = a*sin(t-t1) + bsin(2t-t2) + csin(3t-t3) + 1.

    Parameters
    ----------
    t: numpy float
        defines the range of the period
    a, b, c: float
        constants for sine amplitude
    t1, t2, t3: numpy float
        arbitrary angle values

    Returns
    ----------
    f: numpy array
        linear combination of periodic functions

    '''
    f = (a*np.sin(t - t1)) + (b*np.sin(2*t - t2)) + (c*np.sin(3*t - t3)) + (d*1)
    return f

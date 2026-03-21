import numpy as np
from scipy import optimize

def PeriodicSineFit(t, t1, c, 
                    A0, A1, A2, A3,
                    ):
    '''
    Periodic fitting function for a large dataset.
    
    Parameters
    ----------
    t: numpy array
        angle array values of data
    t1: numpy float
        offset value 
    c: float
        offset term
    A0, A1, A2, A3: float
        associated amplitudes for each sin term, respectively
    t1, t2, t3, t4: 
        angular offset values

    Returns
    ----------
    fs: numpy array
        array values of the evaluated fourier series
    '''
    fs = c + A0*np.sin(t - t1) + A1*np.sin(t - t1) + A2*np.sin(t - t1) + A3*np.sin(t - t1)
    return fs

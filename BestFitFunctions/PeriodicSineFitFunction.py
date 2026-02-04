import numpy as np

def PeriodicSineFit(x, c, A0, A1, A2, A3):
    '''
    Defining a fourier series, periodic function for fitting
    x is the angle/ x-axis data
    c is the offset term
    A0, A1, A2, A3 are the associated amplitudes for each sin term, respectivily 
    
    Data types:
    x: numpy array
    c: float
    A0, A1, A2, A3: float
    return: numpy array
    '''
    return c + A0*np.sin(x/2) + A1*np.sin(2*x/2) + A2*np.sin(3*x/2) + A3*np.sin(4*x/2)

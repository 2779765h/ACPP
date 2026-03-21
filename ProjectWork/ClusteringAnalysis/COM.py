import numpy as np

def COM_X(m,x):
    '''
    Calculates COM for x-coordinate

    Data types:
    m: int or numpy array
    x: numpy array
    return: float
    '''
    return (np.sum(m * x)) / np.sum(m)

def COM_Y(m,y):
    '''
    Calculates COM for y-coordinate

    Data types:
    m: int or numpy array
    y: numpy array
    return: float
    '''
    return (np.sum(m * y)) / np.sum(m)

def Cluster_COM(Data, Range, label, c1, c2, c3, Weight=True):
    '''
    Calculates COM for every cluster in a clustering graph
    
    Data types:
    Data: numpy array
    Range: numpy array
    label: numpy array
        this corresponds to the clustering type, so for DBSCAN use db.labels_

    c1: int
    c2: int
    c3: int
        c indicates the column index
        
    Weight: bool
        if True, applies pixel weighting to the centre of masses

    return: list
    '''
    COM_Values = []

    # loop over all clusters
    for p in Range:
        Cluster = Data[np.where(label == p)]

        if Weight:
            # COM weighting
            COM_Values.append((
                COM_X(Cluster[:,c1], Cluster[:,c2]),
                COM_Y(Cluster[:,c1], Cluster[:,c3])
            ))

        else:
            #COM no weighting
            COM_Values.append((
                COM_X(1, Cluster[:,c2]),
                COM_Y(1, Cluster[:,c3])
            ))
            
    return COM_Values

import numpy as np

def COM_X(m,x):
    '''
    Calculates COM for the x-coordinate of the data

    Parameters
    ----------
    m: numpy array
        adds weighting to the data
    x: numpy array
        x coordinate of the dataset

    Returns
    ----------
    float
        centre of mass value for x coordinate of each cluster
    '''
    return (np.sum(m * x)) / np.sum(m)

def COM_Y(m,y):
    '''
    Calculates COM for the y-coordinate of the data

    Parameters
    ----------
    m: numpy array
        adds weighting to the data
    y: numpy array
        y coordinate of the dataset

    Returns
    ----------
    float
        centre of mass value for x coordinate of each cluster
    '''
    return (np.sum(m * y)) / np.sum(m)

def Cluster_COM(Data, Range, label, Weight=True):
    '''
    Calculates the COM for every cluster in the real space clustering graph

    Parameters
    ----------
    Data: numpy array
        dataset used for clustering
    Range: numpy array
        loop over the range of the cluster labels
    label: numpy array
        dbscan clustering labels, i.e. db.labels
    Weight: bool
        if True, applies pixel weighting to the centre of masses

    Returns
    ----------
    COM_Values: list
        list of centre of mass values
    '''
    COM_Values = []

    # loop over all clusters
    for p in Range:
        Cluster = Data[np.where(label == p)]

        if Weight:
            # COM weighting
            COM_Values.append((
                COM_X(Cluster[:,2], Cluster[:,3]),
                COM_Y(Cluster[:,2], Cluster[:,4])
            ))

        else:
            #COM no weighting
            COM_Values.append((
                COM_X(1, Cluster[:,3]),
                COM_Y(1, Cluster[:,4])
            ))
            
    return COM_Values

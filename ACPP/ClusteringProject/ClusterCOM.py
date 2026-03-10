# find COM for each cluster

def COM_X(m,x):
    m = np.array(m)
    x = np.array(x)
    return (np.sum(m * x)) / np.sum(m)

def COM_Y(m,y):
    m = np.array(m)
    y = np.array(y)
    return (np.sum(m * y)) / np.sum(m)

def Cluster_COM(Data, Range, Weight=True):
    COM_Values = []

    # loop over all clusters
    for p in Range: # loop over the number of clusters
        Cluster = Data[np.where(db.labels_ == p)]

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

import numpy as np
import matplotlib.pyplot as plt

def VirtualImage(ClusterType, ClusterIndex, Data, Rx_col, Ry_col):
    '''
    Function for plotting the image of a clustered pixel in the real space from reciprocal space.
    Cluster types extract the label from the specified clustering algorithm.

    Data types
    ----------
    ClusterType: String (if db = DBSCAN, then enter db, if k = KMEANS, then k etc.)
    ClusterIndex: Int
    Data: numpy array
    Rx_col: Int (corresponds to the column in the dataset)
    Ry_col: Int 

    Returns
    ----------
    matplotlib figure
    '''
    # Select a specific cluster points
    Cluster = Data[np.where(ClusterType.labels_ == ClusterIndex)]

    Rx = Cluster[:, Rx_col]
    Ry = Cluster[:, Ry_col]

    # Finding max dimensions of Rx, Ry
    Rxmax, Rymax = Rx.max().astype('int')+1, Ry.max().astype('int')+1

    # Create image 
    image = np.zeros(shape=(Rxmax,Rymax))
    image[Cluster[:, Rx_col].astype('int'), Cluster[:, Ry_col].astype('int')] = Cluster[:,2]

    # Plot
    plt.figure(figsize=[7,7])
    plt.imshow(image)
    plt.show()

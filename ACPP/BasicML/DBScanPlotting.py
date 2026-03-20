import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from colorsys import hsv_to_rgb

def DBScanClustering(Data, ScalingArray,
                     eps, min_samples, 
                     c1, c2, 
                     xlabel, ylabel,
                     savefig = True):
    '''
    Function which applies DBSCAN clustering to a dataset 
    and plots a clustering graph from selected data arrays. 

    Parameters:
    Data: numpy array
    ScalingArray: numpy array
    eps: int
    min_samples: int
    c1: int
    c2: int
    xlabel: string
    ylabel: string
    savefig: bool
        if True, figure is saved as a graphics file

    Return:
    '''

    # DBScan
    db = DBSCAN(eps=eps, min_samples=min_samples).fit(Data*ScalingArray)
    
    # Colour scheme
    colours = []
    r = db.labels_.max()+1
    d = 5

    for n in range(r):
        h, v = int(n/d), n%d
        H = h/(r/d)
        V = (4+v)/8
        S = 1
        c = hsv_to_rgb(H,S,V)
        colours += [c] 
    
    # Plot
    fig, ax = plt.subplots(figsize=[8,8])
    ax.set_title('DBScan Clustering')

    for i in range(r):   
        Cluster = Data[np.where(db.labels_ == i)]
        scatter = ax.scatter(Cluster[:, c1], Cluster[:, c2], color=colours[i], label = i, s=5, alpha=1)
    
        for n in range(0,Cluster.shape[0],4500): # number of iterations 
            ax.text(
                Cluster[n, c1], 
                Cluster[n, c2]+3, 
                int(i),
                horizontalalignment='center'
            )

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
                       
    if savefig:
        plt.savefig('DBSCANClusteringPlot')


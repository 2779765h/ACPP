import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from colorsys import hsv_to_rgb

def DBScanClustering(Data, dblabels,
                     c1, c2, 
                     xlabel, ylabel, Title,
                     offset,
                     savefig = True):
    '''
    A function that plots a clustering graph from selected data arrays,
    after DBSCAN has been applied to a dataset. 
    
    Parameters
    ----------
    Data: numpy array
        dataset used for the DBSCAN algorithm
    dblabels: numpy array
        labels from dbscan clusters, i.e. db.labels_
    c1, c2: int
        column indices to select from the data array
    xlabel, ylabel: string
        labels for the x and y axes
    Title: string
        title for the plot
    offset: float
        offset can be used to adjust the spacing of labels from the data
    savefig: bool
        if True, the figure is saved as 'DBSCANClusteringPlot'

    Returns
    ----------
    None
    '''
    # Colour scheme
    colours = []
    r = dblabels.max()+1
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
    ax.set_title(Title)

    for i in range(r):   
        Cluster = Data[np.where(dblabels == i)]
        scatter = ax.scatter(Cluster[:, c1], Cluster[:, c2], color=colours[i], label = i, s=5, alpha=1)
    
        for n in range(0,Cluster.shape[0],4500): # number of iterations 
            ax.text(
                Cluster[n, c1], 
                Cluster[n, c2]+offset, 
                int(i),
                horizontalalignment='center'
            )

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
                       
    if savefig:
        plt.savefig('DBSCANClusteringPlot')

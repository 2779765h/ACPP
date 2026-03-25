import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from colorsys import hsv_to_rgb

def KMeansClustering(Data, klabels,
                     c1, c2, 
                     xlabel, ylabel, Title,
                     offset,
                     savefig = True):
    '''
    A function that plots a clustering graph from selected data arrays,
    after KMeans has been applied to a dataset. 
    
    Parameters
    ----------
    Data: numpy array
        dataset used for the KMeans algorithm
    klabels: numpy array
        labels from kmeans clusters, i.e. k.labels_
    c1, c2: int
        column indices to select from the data array
    xlabel, ylabel: string
        labels for the x and y axes
    Title: string
        title for the plot
    offset: float
        offset can be used to adjust the spacing of labels from the data
    savefig: bool
        if True, the figure is saved as 'KMeansClusteringPlot'

    Returns
    ----------
    None
    '''
    # Colour scheme
    colours = []
    r = k.labels_.max()+1
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

    ax.set_title('KMeans Clustering')

    for i in range(r):   
        Cluster = Data[np.where(k.labels_ == i)]
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
        plt.savefig('KMeansClusteringPlot')

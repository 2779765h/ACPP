import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from colorsys import hls_to_rgb, hsv_to_rgb

def KMeansClustering(Data, r):
    '''
    Function to apply KMeans clustering onto dataset.

    Data types:
    Data: np array
    r: integer

    Return:
    Matplotlib plot
    '''
    
    # Colours
    colours = []
    d = 5
    for n in range(r):
        h, v = int(n/d), n%d
        H = h/(r/d)
        V = (4+v)/8
        S = 1
        c = hsv_to_rgb(H,S,V)
        colours += [c] 
    
    # Data
    Qx = data[:,0]
    Qy = data[:,1]

    # Apply KMeans
    k = KMeans(n_clusters=r).fit(data[:,:2])

    # Plot
    plt.figure(figsize=[10,10])
    plt.title('KMeans Clustering')
    
    for i in range(r):   
        Cluster = data[np.where(k.labels_ == i)]
        scatter = plt.scatter(Cluster[:, 0], Cluster[:, 1], color=colours[i], label = i)
    
        for n in range(0, Cluster.shape[0], 4500): # number of iterations 
            plt.text(
                Cluster[n, 0], 
                Cluster[n, 1]+3, 
                int(i),
                horizontalalignment='center'
            )

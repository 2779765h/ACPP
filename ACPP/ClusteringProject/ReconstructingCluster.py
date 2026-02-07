import numpy as np
import matplotlib.pyplot as plt

def ReconstructedImage(ClusterType, ClusterIndex, Title):
    '''
    Function for plotting the image of a clustered pixel in the real space from reciprocal space.
    Cluster types extract the label from the specified clustering algorithm.

    Data types:
    ClusterType: String (if db = DBSCAN, then enter db, if k = KMEANS, then k etc.)
    ClusterIndex: Int
    Title: String
    '''
    # Finding max dimensions of Qx, Qy
    Qxmax, Qymax = data[:,3].max().astype('int')+1, data[:,4].max().astype('int')+1

    # Select a specific cluster points
    Cluster = data[np.where(ClusterType.labels_ == ClusterIndex)]

    # Create image 
    image = np.zeros(shape=(Qxmax,Qymax))
    image[Cluster[:,3].astype('int'),Cluster[:,4].astype('int')] = Cluster[:,2]

    # Plot
    plt.figure(figsize=[8,8])
    plt.title(Title)
    plt.imshow(image)
    plt.xlabel('Rx')
    plt.ylabel('Ry')
    plt.show()

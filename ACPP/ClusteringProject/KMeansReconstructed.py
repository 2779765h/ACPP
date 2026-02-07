import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def ReconstructedImage(ClusterIndex, Title):
    '''
    Function for plotting the image of a clustered pixel in the real space from reciprocal space

    Data types:
    ClusterIndex: Int
    Title: String
    '''
    # Finding max dimensions of Qx, Qy
    Qxmax, Qymax = data[:,3].max().astype('int')+1, data[:,4].max().astype('int')+1

    # Select a specific cluster points
    Cluster = data[np.where(k.labels_ == ClusterIndex)]

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

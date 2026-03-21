import numpy as np
import matplotlib.pyplot as plt

def VirtualImage(Data, Label, Index, savefig = True, figax = None):
    '''
    Function which produces the Digital Dark Field Image of a selected cluster.

    Parameters
    ----------
    Data: numpy array
        dataset used for clustering
    Label: numpy array
        clustering labels, i.e. for DBSCAN use db.labels_
    Index: Int
        select the index of the cluster
    savefig: bool
        if True, the figure is saved as 'DigitalDarkFieldImage'
    figax: tuple, None
        (fig, ax)

    Returns
    ----------
    None
    '''
    Cluster = Data[np.where(Label == Index)]

    Rxc = Cluster[:, 3]
    Ryc = Cluster[:, 4]

    # Finding max dimensions of Rx, Ry
    Rxmax, Rymax = Data[:,3].max().astype('int')+1, Data[:,4].max().astype('int')+1
    
    # Create image 
    image = np.zeros(shape=(Rxmax,Rymax))
    image[Rxc.astype('int'), Ryc.astype('int')]  = Cluster[:,2]

    # Plot
    if figax != None:
        fig, ax = figax
    else:
        fig, ax = plt.subplots(figsize=[7,7])

    ax.imshow(image)
      
    ax.set_xlabel('Ry')
    ax.set_ylabel('Rx')

    plt.show()
         
    if savefig:
        fig.savefig('DigitalDarkFieldImage')

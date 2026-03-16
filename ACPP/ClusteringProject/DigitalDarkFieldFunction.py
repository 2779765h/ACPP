import numpy as np

def VirtualImage(Data, Label, Index, x, y, Rx, Ry, savefig = True):
    '''
    Function which produces the Digital Dark Field Image of a selected cluster.

    Data types:
    Data: numpy array
    Label: numpy array
        this corresponds to the clustering type, so for DBSCAN use db.labels_
        
    Index: Int
        select the index of the cluster
    x: Int 
    y: Int 
    Rx: numpy array
    Ry: numpy array

    Return: NoneType
        virtual image of cluster
    '''
    Cluster = Data[np.where(Label == Index)]

    Rxc = Cluster[:, x]
    Ryc = Cluster[:, y]

    # Finding max dimensions of Rx, Ry
    Rxmax, Rymax = Rx.max().astype('int')+1, Ry.max().astype('int')+1
    
    # Create image 
    image = np.zeros(shape=(Rxmax,Rymax))
    image[Rxc.astype('int'), Ryc.astype('int')]  = Cluster[:,1]

    # Plot
    fig, ax = plt.subplots(figsize=[7,7])

    ax.imshow(image)
      
    ax.set_xlabel('Ry')
    ax.set_ylabel('Rx')

    plt.show()
         
    if savefig:
        fig.savefig('DigitalDarkFieldImage')

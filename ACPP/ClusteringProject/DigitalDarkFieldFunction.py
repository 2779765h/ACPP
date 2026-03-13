import numpy as np

def VirtualImage(Data, Label, Index, x, y, Rx, Ry):
    '''
    Function which produces the Digital Dark Field Image of a selected cluster

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
    returns: NoneType
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
    plt.figure(figsize=[7,7])
    plt.title('Virtual Image for Cluster H')
    plt.xlabel('Ry')
    plt.ylabel('Rx')
    plt.imshow(image)
    plt.show()

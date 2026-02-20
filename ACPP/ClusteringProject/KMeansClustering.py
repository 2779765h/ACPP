import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from colorsys import hsv_to_rgb

# Colours
colours = []
r = 60
d = 5
for n in range(r):
    # integers
    h, v = int(n/d), n%d 
    # normalisation
    H = h/(r/d)
    V = (4+v)/8
    S = 1
    c = hsv_to_rgb(H,S,V)
    colours += [c] 

# Apply KMeans
k = KMeans(n_clusters=r).fit(data[:,:2])

# Plot
plt.figure(figsize=[10,10])
plt.title('KMeans Clustering')
for i in range(r):
    Cluster = data[np.where(k.labels_ == i)]
    scatter = plt.scatter(Cluster[:, 0], Cluster[:, 1], color=colours[i], label = i)
    
    for n in range(0,Cluster.shape[0],4500): # number of iterations 
        plt.text(
            Cluster[n, 0], 
            Cluster[n, 1]+3, 
            int(i),
            horizontalalignment='center'
        )
    plt.xlabel("Qx")
    plt.ylabel("Qy")

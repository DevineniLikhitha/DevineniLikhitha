from sklearn import datasets
from sklearn.datasets import fetch_openml
import pandas as pd
import random
from sklearn.metrics import silhouette_samples, silhouette_score
import numpy as np
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import fcluster
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram
from matplotlib import cm

import time
class data:
    mnist = fetch_openml('mnist_784', version=1)
    
    X, y = mnist['data'], mnist['target']
   
    
    df = pd.DataFrame(mnist.data, columns = mnist.feature_names)
    y=pd.DataFrame(y)
   
    
    
  
    
 
    
   
    sample=df.take(np.random.permutation(len(df))[:1000])
    sample_y=y.take(np.random.permutation(len(df))[:1000])
    
    print(sample)
    #print(np.unique(y))
    print(np.unique(sample_y))
    
    
    print(sample.shape)

start_time = time.time()



class Kmeans:
    
    mnist = fetch_openml('mnist_784', version=1)
    
    #X=mnist.data
    
    
    
    df = pd.DataFrame(mnist.data, columns = mnist.feature_names)
    
    
    
    sample=df.take(np.random.permutation(len(df))[:1000])
    
    #model fitting
    km = KMeans(n_clusters=10, init='random',  n_init=10, max_iter=300, tol=1e-04, random_state=0)
    y_km = km.fit_predict(sample)
    print(y_km)
    print(km.cluster_centers_ )
    print('Distortion: %.2f' % km.inertia_)
    print('silhoutte score k means -mnist',silhouette_score(sample,y_km))
    #silhoutte graph
    cluster_labels = np.unique(y_km)
    n_clusters = cluster_labels.shape[0]
    silhouette_vals = silhouette_samples(sample, y_km, metric='euclidean')
    y_ax_lower, y_ax_upper = 0, 0
    yticks = []
    for i, c in enumerate(cluster_labels):
        c_silhouette_vals = silhouette_vals[y_km == c]
        c_silhouette_vals.sort()
        y_ax_upper += len(c_silhouette_vals)
        color = cm.jet(float(i) / n_clusters)
        plt.barh(range(y_ax_lower, y_ax_upper), c_silhouette_vals, height=1.0, 
                 edgecolor='none', color=color)
    
        yticks.append((y_ax_lower + y_ax_upper) / 2.)
        y_ax_lower += len(c_silhouette_vals)
        
    silhouette_avg = np.mean(silhouette_vals)
    plt.axvline(silhouette_avg, color="red", linestyle="--") 
    
    plt.yticks(yticks, cluster_labels + 1)
    plt.ylabel('Cluster')
    plt.xlabel('Silhouette coefficient')
    
    plt.tight_layout()
    
    plt.show()
print("--- %s seconds for sklearn ---" % (time.time() - start_time))     
#calculating k using elbow approach   
class elbow:
    
    mnist = fetch_openml('mnist_784', version=1)
    
    #X=mnist.data
    
    
    
    df = pd.DataFrame(mnist.data, columns = mnist.feature_names)
    
    
    
    sample=df.take(np.random.permutation(len(df))[:1000])


    distortions = []
    # Calculate distortions
    for i in range(1, 17):
        km = KMeans(n_clusters=i, 
        init='k-means++', 
        n_init=10, 
        max_iter=300, 
        random_state=0)
        km.fit(sample)
        distortions.append(km.inertia_)
        
    #Plot distortions for different K
    plt.plot(range(1, 17), distortions, marker='o')
    plt.xlabel('Number of clusters')
    plt.ylabel('Distortion')
    plt.tight_layout()
    plt.show()
start_time = time.time()
class Hirarcheal_scipy:
    
    mnist = fetch_openml('mnist_784', version=1)
    
    #X=mnist.data
    
    
    
    df = pd.DataFrame(mnist.data, columns = mnist.feature_names)
    
    
    
    sample=df.take(np.random.permutation(len(df))[:1000])
    row_cluster1 = linkage(sample.values, method='average', metric='euclidean') 
    #print(row_cluster1)
    #dn = dendrogram(row_cluster1, above_threshold_color="green", color_threshold=.7, orientation='right')
    row_dendr = dendrogram(row_cluster1) 
    
  
    plt.tight_layout()
    plt.ylabel('Euclidean distance') 
    plt.show()
    
    k=10
    #model fitting
    
    fclust = fcluster(row_cluster1, k, criterion='maxclust')
   
    
    print(fclust)
    print('silhoutte score hirarcheal scipy-mnist',silhouette_score(sample, fclust))
    #silhoutte graph
    cluster_labels = np.unique(fclust)
    n_clusters = cluster_labels.shape[0]
    silhouette_vals = silhouette_samples(sample, fclust, metric='euclidean')
    y_ax_lower, y_ax_upper = 0, 0
    yticks = []
    for i, c in enumerate(cluster_labels):
        c_silhouette_vals = silhouette_vals[fclust == c]
        c_silhouette_vals.sort()
        y_ax_upper += len(c_silhouette_vals)
        color = cm.jet(float(i) / n_clusters)
        plt.barh(range(y_ax_lower, y_ax_upper), c_silhouette_vals, height=1.0, 
                 edgecolor='none', color=color)
    
        yticks.append((y_ax_lower + y_ax_upper) / 2.)
        y_ax_lower += len(c_silhouette_vals)
        
    silhouette_avg = np.mean(silhouette_vals)
    plt.axvline(silhouette_avg, color="red", linestyle="--") 
    
    plt.yticks(yticks, cluster_labels + 1)
    plt.ylabel('Cluster')
    plt.xlabel('Silhouette coefficient-scipy')
    
    plt.tight_layout()
    
    plt.show()
print("--- %s seconds for sklearn ---" % (time.time() - start_time)) 
start_time = time.time()
class Hirarcheal_sklearn:
        
    mnist = fetch_openml('mnist_784', version=1)
    
    #X=mnist.data
    
    
    
    df = pd.DataFrame(mnist.data, columns = mnist.feature_names)
    
    
    
    sample=df.take(np.random.permutation(len(df))[:1000])

     #model fitting 
    cluster1 = AgglomerativeClustering(n_clusters=10, affinity='euclidean', linkage='complete')
    cluster1_labels = cluster1.fit_predict(sample)
    print(cluster1_labels)
    print('silhoutte score hirarcheal sklearn - mnist',silhouette_score(sample, cluster1_labels))
    #silhoutte graph
    cluster_labels = np.unique(cluster1_labels)
    n_clusters = cluster_labels.shape[0]
    silhouette_vals = silhouette_samples(sample, cluster1_labels, metric='euclidean')
    y_ax_lower, y_ax_upper = 0, 0
    yticks = []
    for i, c in enumerate(cluster_labels):
        c_silhouette_vals = silhouette_vals[cluster1_labels == c]
        c_silhouette_vals.sort()
        y_ax_upper += len(c_silhouette_vals)
        color = cm.jet(float(i) / n_clusters)
        plt.barh(range(y_ax_lower, y_ax_upper), c_silhouette_vals, height=1.0, 
                 edgecolor='none', color=color)
    
        yticks.append((y_ax_lower + y_ax_upper) / 2.)
        y_ax_lower += len(c_silhouette_vals)
        
    silhouette_avg = np.mean(silhouette_vals)
    plt.axvline(silhouette_avg, color="red", linestyle="--") 
    
    plt.yticks(yticks, cluster_labels + 1)
    plt.ylabel('Cluster')
    plt.xlabel('Silhouette coefficient-sklearn')
    
    plt.tight_layout()
    
    plt.show()

print("--- %s seconds for sklearn ---" % (time.time() - start_time)) 
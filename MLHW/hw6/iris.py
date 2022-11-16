from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import fcluster    
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from sklearn.metrics import accuracy_score
import scipy.cluster.hierarchy as shc
import time

class data:
    df=pd.read_csv('iris.data.txt',header=None,sep=",")
    df.columns=["sepallength","sepalwidth","petallength","petalwidth","species"]
    X= df[['sepallength','sepalwidth','petallength','petalwidth']]
    y=df[['species']]
    print(X.shape)
    irissetosa = y.loc[y["species"]=="Iris-setosa"]
    
    #count no.of rows that have iris-setosa
    iris_setosa_rows=len(irissetosa)
    
    #printing the no.of rows that iris-setosa as last column
    print("No.of iris-setosa rows->",iris_setosa_rows)
    
    #iris-virginica
    irisvirginica = y.loc[y["species"]=="Iris-virginica"]
    
    #count no.of rows that have iris-virginica
    iris_virginica_rows=len(irisvirginica)
    
    #printing the no.of rows that iris-viriginica as last column
    print("No.of iris-virginica rows->",iris_virginica_rows)
    
    #iris-versicolor
    irisversicolor = y.loc[y["species"]=="Iris-versicolor"]
    
    #count no.of rows that have iris-versicolor
    iris_versicolor_rows=len(irisversicolor)
    
    #printing the no.of rows that iris-versicolor as last column
    print("No.of iris-virginica rows->",iris_versicolor_rows)
    
    distinct=y.species.unique()
    print("unique values of lastcolumn->",distinct)

start_time = time.time()
#Kmeans clustering
class Kmeans:
    df=pd.read_csv('iris.data.txt',header=None,sep=",")
    df.columns=["sepallength","sepalwidth","petallength","petalwidth","species"]
    X= df[['sepallength','sepalwidth','petallength','petalwidth']]
    y=df[['species']]
    km = KMeans(n_clusters=3, init='random',  n_init=10, max_iter=300, tol=1e-04, random_state=0)
    y_km = km.fit_predict(X)
    print(y_km)
    print(km.cluster_centers_ )
    print('Distortion: %.2f' % km.inertia_)
    print('silhoutte score k means - iris',silhouette_score(X,y_km))
    
    cluster_labels = np.unique(y_km)
    n_clusters = cluster_labels.shape[0]
    silhouette_vals = silhouette_samples(X, y_km, metric='euclidean')
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
print("--- %s seconds for kmeans  ---" % (time.time() - start_time))   



#Hirarcheal Scipy
start_time = time.time()
class Hirarcheal_scipy:
    df=pd.read_csv('iris.data.txt',header=None,sep=",")
    df.columns=["sepallength","sepalwidth","petallength","petalwidth","species"]
    X= df[['sepallength','sepalwidth','petallength','petalwidth']]
    y=df[['species']]

    row_cluster1 = linkage(X.values, method='average', metric='euclidean') 
    #print(row_cluster1)
    #dn = dendrogram(row_cluster1, above_threshold_color="green", color_threshold=.7, orientation='right')
    row_dendr = dendrogram(row_cluster1) 
    
  
    plt.tight_layout()
    plt.ylabel('Euclidean distance') 
    plt.show()
    
    k=3
    
    fclust = fcluster(row_cluster1, k, criterion='maxclust')
   
    
    print(fclust)
    print('silhoutte score hirarcheal scipy - iris',silhouette_score(X, fclust))
    
    cluster_labels = np.unique(fclust)
    n_clusters = cluster_labels.shape[0]
    silhouette_vals = silhouette_samples(X, fclust, metric='euclidean')
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
    
    
print("--- %s seconds for scipy ---" % (time.time() - start_time))    
 
#hirarcheal sklearn
start_time = time.time()
class Hirarcheal_sklearn:
    df=pd.read_csv('iris.data.txt',header=None,sep=",")
    df.columns=["sepallength","sepalwidth","petallength","petalwidth","species"]
    X= df[['sepallength','sepalwidth','petallength','petalwidth']]
    y=df[['species']]


    cluster1 = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='complete')
    cluster1_labels = cluster1.fit_predict(X)
    print(cluster1_labels)
    print('silhoutte score hirarcheal sklearn - iris',silhouette_score(X, cluster1_labels))
    
    cluster_labels = np.unique(cluster1_labels)
    n_clusters = cluster_labels.shape[0]
    silhouette_vals = silhouette_samples(X, cluster1_labels, metric='euclidean')
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
#calculating k using elbow approach   
class elbow:
    df=pd.read_csv('iris.data.txt',header=None,sep=",")
    df.columns=["sepallength","sepalwidth","petallength","petalwidth","species"]
    X= df[['sepallength','sepalwidth','petallength','petalwidth']]
    y=df[['species']]


    distortions = []
    # Calculate distortions
    for i in range(1, 11):
        km = KMeans(n_clusters=i, 
        init='k-means++', 
        n_init=10, 
        max_iter=300, 
        random_state=0)
        km.fit(X)
        distortions.append(km.inertia_)
        
    #Plot distortions for different K
    plt.plot(range(1, 11), distortions, marker='o')
    plt.xlabel('Number of clusters')
    plt.ylabel('Distortion')
    plt.tight_layout()
    plt.show()
    
    

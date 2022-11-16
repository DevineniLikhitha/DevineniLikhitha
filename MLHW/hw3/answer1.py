from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import StandardScaler
from matplotlib.colors import ListedColormap
from sklearn.metrics import classification_report
from sklearn.datasets import make_classification
from sklearn import svm
from sklearn.svm import SVC
from distutils.version import LooseVersion
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn import tree
import matplotlib
import random


def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):

    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], 
                    y=X[y == cl, 1],
                    alpha=0.8, 
                    color=colors[idx],
                    marker=markers[idx], 
                    label=cl, 
                    edgecolor='black')

    # highlight test examples
    if test_idx:
        # plot all examples
        X_test, y_test = X[test_idx, :], y[test_idx]

        
        if LooseVersion(matplotlib.__version__) < LooseVersion('0.3.4'):
            plt.scatter(X_test[:, 0],
                        X_test[:, 1],
                        c='',
                        edgecolor='black',
                        alpha=1.0,
                        linewidth=1,
                        marker='o',
                        s=100, 
                        label='test set')
        else:
            plt.scatter(X_test[:, 0],
                        X_test[:, 1],
                        c='none',
                        edgecolor='black',
                        alpha=1.0,
                        linewidth=1,
                        marker='o',
                        s=100, 
                        label='test set')      


class perceptron:
    #loading iris dataset
    
    iris = datasets.load_iris()
    X = iris.data[:, [2, 3]]
    y = iris.target
    
    print('Class labels:', np.unique(y))
    
    # Splitting data into 70% training and 30% test data:
    
    
    
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1, stratify=y)
    
    print('Labels count in y:', np.bincount(y))
    print('Labels count in y_train:', np.bincount(y_train))
    print('Labels count in y_test:', np.bincount(y_test))
    

    
    
    
    # ## Training a perceptron via scikit-learn
    
    
    ppn = Perceptron(max_iter=10,eta0=0.1, random_state=1)
    ppn.fit(X_train, y_train)
    
    y_pred = ppn.predict(X_test)
    print('Misclassified examples: %d' % (y_test != y_pred).sum())
    
    
    #predictions
    
    sample = random.sample(range(len(X_train)),10)
    for i in sample:
        print(i,ppn.predict([X_train[i]]))
        
    #classification report for training data
    
    print(classification_report(ppn.predict(X_train),y_train))
    
    #classificaton report for test data
    
    print(classification_report(ppn.predict(X_test),y_test))
    
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)
    
    X_combined_std = np.vstack((X_train_std, X_test_std))
    y_combined = np.hstack((y_train, y_test))
    
    plot_decision_regions(X=X_combined_std, y=y_combined,
                      classifier=ppn, test_idx=range(105, 150))
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()
    


class linearSVC:
    iris = datasets.load_iris()
    X = iris.data[:, [2, 3]]
    y = iris.target
    
    print('Class labels:', np.unique(y))
    
    # Splitting data into 70% training and 30% test data:
    
    
    
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1, stratify=y)
    
    #Train the model
    lsvm = svm.SVC(kernel='linear')
    
    lsvm.fit(X_train,y_train)
    score = lsvm.score(X_train,y_train)
    print('Accuracy score',score)
    
    #cross_val_score
    
    c_v_score = cross_val_score(lsvm,X_train,y_train, cv=10)
    print("CV score: %.2f" % c_v_score.mean())
    
    y_pred= lsvm.predict(X_test)
    
    #confusion matrix
    
    c_m = confusion_matrix(y_test, y_pred)
    print(c_m)
    
    #classification report
    
    print(classification_report(y_test,y_pred))
    
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)
    
    X_combined_std = np.vstack((X_train_std, X_test_std))
    y_combined = np.hstack((y_train, y_test))
    
    
    plot_decision_regions(X=X_combined_std, y=y_combined,
                      classifier=lsvm, test_idx=range(105, 150))
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()
    
class rbfkernel:
    iris = datasets.load_iris()
    X = iris.data[:, [2, 3]]
    y = iris.target
    
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1, stratify=y)
    
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)
    
 

    X_combined_std = np.vstack((X_train_std, X_test_std))
    y_combined = np.hstack((y_train, y_test))


    svm = SVC(kernel='rbf', random_state=1, gamma=0.2, C=1.0)
    svm.fit(X_train_std, y_train)
    
    score = svm.score(X_train,y_train)
    print('Accuracy score',score)
    
    #cross_val_score
    
    c_v_score = cross_val_score(svm,X_train,y_train, cv=10)
    print("CV score: %.2f" % c_v_score.mean())
    
    y_pred= svm.predict(X_test)
    
    #confusion matrix
    
    c_m = confusion_matrix(y_test, y_pred)
    print(c_m)
    
    #classification report
    
    print(classification_report(y_test,y_pred))
    
    
    plot_decision_regions(X_combined_std, y_combined,
                          classifier=svm, test_idx=range(105, 150))
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()




class decisontree:
    iris = datasets.load_iris()
    X = iris.data[:, [2, 3]]
    y = iris.target
    
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1, stratify=y)
    
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)
    
 

    X_combined_std = np.vstack((X_train_std, X_test_std))
    y_combined = np.hstack((y_train, y_test))
    
    tree_model = DecisionTreeClassifier(criterion='gini', 
                                        max_depth=4, 
                                        random_state=1)
    tree_model.fit(X_train, y_train)
    
    X_combined = np.vstack((X_train, X_test))
    y_combined = np.hstack((y_train, y_test))
    plot_decision_regions(X_combined, y_combined, 
                          classifier=tree_model,
                          test_idx=range(105, 150))
    
    plt.xlabel('petal length [cm]')
    plt.ylabel('petal width [cm]')
    plt.legend(loc='upper left')
    plt.tight_layout()

    plt.show()
    
    tree.plot_tree(tree_model)

    plt.show()




    
    

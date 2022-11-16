import numpy as np
from numpy.random import seed
import pandas as pd
import matplotlib.pyplot as plt
class onevsrest:
 
    class SGD1(object):
    
    	def __init__(self, eta = 0.01, n_iter = 10, shuffle= True,
    				random_state = None):
    
    		self.eta = eta
    		self.n_iter = n_iter
    		self.w_initialization = False
    		self.shuffle = shuffle
    
    		if random_state:
    			seed(random_state)
    
    	def fit(self, X, y):
    
    		
    		self._initialize_weights(X.shape[1])
    		self.cost_ = []
    
    		for i in range(self.n_iter):
    
    			if self.shuffle:
    				X, y = self._shuffle(X, y)
    
    			cost = []
    			for xi, target in zip(X, y):
    				cost.append(self._update_weights(xi, target))
    
    			avg_cost = sum(cost) / len(y)
    			self.cost_.append(avg_cost)
    
    		return self
    
    	def partial_fit(self, X, y):
    
    		""" Fit training data without reinitializing the weights """
    
    		if not self.w_initialized:
    			self._initialize_weights(X.shape[1])
    
    		if y.ravel().shape[0] > 1:
    
    			for xi, target in zip(X, y):
    				self._update_weights(xi, target)
    		else:
    			self._update_weights(X, y)
    
    		return self
    
    	def _shuffle(self, X, y):
    
    		""" Shuffle training data """
    
    		r = np.random.permutation(len(y))
    
    		return X[r], y[r]
    
    	def _initialize_weights(self, m):
    
    		""" Initialize weights to zeros """
    
    		self.w_ = np.zeros(1 + m)
    		self.w_initialized = True
    
    	def _update_weights(self, xi, target):
    
    		""" Apply Adaline learning rule to update the weights """
    
    		output = self.net_input(xi)
    		error = (target - output)
    		self.w_[1:] += self.eta * xi.dot(error)
    		self.w_[0] += self.eta * error
    		cost = 0.5 * (error ** 2)
    
    		return cost
    
    	def net_input(self, X):
    
    		""" Calculate net input """
    
    		return np.dot(X, self.w_[1:]) + self.w_[0]
    
    	def activation(self, X):
    
    		""" Compute linear activation """
    
    		return self.net_input(X)
    
    	def predict(self, X):
    
    		""" Return class label after the unit step """
    
    		return np.where(self.activation(X) >= 0.0, 1, -1)
    	def score(self, X, y):
    		misclassified_data_count = 0
    		for xi, target in zip(X, y):
    			output = self.predict(xi)
    			if(target != output):
    				misclassified_data_count += 1
    		total_data_count = len(X)
    		self.score_ = (total_data_count - misclassified_data_count)/total_data_count
    		return self.score_
        
    # Create the AdalineSGD model
    sgd1 = SGD1(n_iter = 15, eta = 0.01, random_state = 1)
    
    # Train the model
    
    
    # Plot the training errors of both of the models
    df = pd.read_csv('iris.data.txt', header=None)
    y = df.iloc[0:150, 4].values
    y = np.where(y == 'Iris-setosa', 1, -1)
    X = df.iloc[0:150, [0, 2]].values
    sgd1.fit(X, y)
    plt.plot(range(1, len(sgd1.cost_) + 1), sgd1.cost_, marker='o')
    plt.xlabel('Epochs')
    plt.ylabel('error-iris-class1')
    plt.tight_layout()
    plt.show()
    print('classifier one  accuracy-iris',sgd1.score(X,y))
    
    
    dataframe = pd.read_csv('wine-red.txt',header=None,sep=';')
    a = dataframe.iloc[0:1599, 11].values
    a = np.where(y == 6, -1, 1)
    B = dataframe.iloc[0:1599, [0, 2]].values
    sgd1a = SGD1(n_iter = 15, eta = 0.01, random_state = 1)
    sgd1a.fit(B, a)
    plt.plot(range(1, len(sgd1a.cost_) + 1), sgd1a.cost_, marker='*')
    plt.xlabel('Epochs')
    plt.ylabel('error-wine-class1')
    plt.tight_layout()
    plt.show()
    print('classifier one  accuracy-wine',sgd1.score(B,a))
    
    
    class SGD2(object):
    
    	def __init__(self, eta = 0.01, n_iter = 10, shuffle= True,
    				random_state = None):
    
    		self.eta = eta
    		self.n_iter = n_iter
    		self.w_initialization = False
    		self.shuffle = shuffle
    
    		if random_state:
    			seed(random_state)
    
    	def fit(self, X, y):
    
    		
    		self._initialize_weights(X.shape[1])
    		self.cost_ = []
    
    		for i in range(self.n_iter):
    
    			if self.shuffle:
    				X, y = self._shuffle(X, y)
    
    			cost = []
    			for xi, target in zip(X, y):
    				cost.append(self._update_weights(xi, target))
    
    			avg_cost = sum(cost) / len(y)
    			self.cost_.append(avg_cost)
    
    		return self
    
    	def partial_fit(self, X, y):
    
    		""" Fit training data without reinitializing the weights """
    
    		if not self.w_initialized:
    			self._initialize_weights(X.shape[1])
    
    		if y.ravel().shape[0] > 1:
    
    			for xi, target in zip(X, y):
    				self._update_weights(xi, target)
    		else:
    			self._update_weights(X, y)
    
    		return self
    
    	def _shuffle(self, X, y):
    
    		""" Shuffle training data """
    
    		r = np.random.permutation(len(y))
    
    		return X[r], y[r]
    
    	def _initialize_weights(self, m):
    
    		""" Initialize weights to zeros """
    
    		self.w_ = np.zeros(1 + m)
    		self.w_initialized = True
    
    	def _update_weights(self, xi, target):
    
    		""" Apply Adaline learning rule to update the weights """
    
    		output = self.net_input(xi)
    		error = (target - output)
    		self.w_[1:] += self.eta * xi.dot(error)
    		self.w_[0] += self.eta * error
    		cost = 0.5 * (error ** 2)
    
    		return cost
    
    	def net_input(self, X):
    
    		""" Calculate net input """
    
    		return np.dot(X, self.w_[1:]) + self.w_[0]
    
    	def activation(self, X):
    
    		""" Compute linear activation """
    
    		return self.net_input(X)
    
    	def predict(self, X):
    
    		""" Return class label after the unit step """
    
    		return np.where(self.activation(X) >= 0.0, 1, -1)
    	def score(self, X, y):
    		misclassified_data_count = 0
    		for xi, target in zip(X, y):
    			output = self.predict(xi)
    			if(target != output):
    				misclassified_data_count += 1
    		total_data_count = len(X)
    		self.score_ = (total_data_count - misclassified_data_count)/total_data_count
    		return self.score_
    # Create the AdalineSGD model
    sgd2 = SGD2(n_iter = 15, eta = 0.01, random_state = 1)
    
    # Train the model
    
    
    # Plot the training errors of both of the models
    df = pd.read_csv('iris.data.txt', header=None)
    y = df.iloc[0:150, 4].values
    y = np.where(y == 'Iris-versicolor', 1, -1)
    X = df.iloc[0:150, [0, 2]].values
    sgd2.fit(X, y)
    plt.plot(range(1, len(sgd2.cost_) + 1), sgd2.cost_, marker='o')
    plt.xlabel('Epochs')
    plt.ylabel('error-iris-class2')
    plt.tight_layout()
    plt.show()
    print('classifier two  accuracy-iris',sgd2.score(X,y))
    
    
    dataframe = pd.read_csv('wine-red.txt',header=None,sep=';')
    a = dataframe.iloc[0:1599, 11].values
    a = np.where(y == 5, -1, 1)
    B = dataframe.iloc[0:1599, [0, 2]].values
    sgd2a = SGD2(n_iter = 25, eta = 0.00001, random_state = 1)
    sgd2a.fit(B, a)
    plt.plot(range(1, len(sgd2a.cost_) + 1), sgd2a.cost_, marker='*')
    plt.xlabel('Epochs')
    plt.ylabel('error-wine-class2')
    plt.tight_layout()
    plt.show()
    print('classifier two  accuracy-wine',sgd2.score(B,a))
    
    
    class SGD3(object):
    
    	def __init__(self, eta = 0.01, n_iter = 10, shuffle= True,
    				random_state = None):
    
    		self.eta = eta
    		self.n_iter = n_iter
    		self.w_initialization = False
    		self.shuffle = shuffle
    
    		if random_state:
    			seed(random_state)
    
    	def fit(self, X, y):
    
    		
    		self._initialize_weights(X.shape[1])
    		self.cost_ = []
    
    		for i in range(self.n_iter):
    
    			if self.shuffle:
    				X, y = self._shuffle(X, y)
    
    			cost = []
    			for xi, target in zip(X, y):
    				cost.append(self._update_weights(xi, target))
    
    			avg_cost = sum(cost) / len(y)
    			self.cost_.append(avg_cost)
    
    		return self
    
    	def partial_fit(self, X, y):
    
    		""" Fit training data without reinitializing the weights """
    
    		if not self.w_initialized:
    			self._initialize_weights(X.shape[1])
    
    		if y.ravel().shape[0] > 1:
    
    			for xi, target in zip(X, y):
    				self._update_weights(xi, target)
    		else:
    			self._update_weights(X, y)
    
    		return self
    
    	def _shuffle(self, X, y):
    
    		""" Shuffle training data """
    
    		r = np.random.permutation(len(y))
    
    		return X[r], y[r]
    
    	def _initialize_weights(self, m):
    
    		""" Initialize weights to zeros """
    
    		self.w_ = np.zeros(1 + m)
    		self.w_initialized = True
    
    	def _update_weights(self, xi, target):
    
    		""" Apply Adaline learning rule to update the weights """
    
    		output = self.net_input(xi)
    		error = (target - output)
    		self.w_[1:] += self.eta * xi.dot(error)
    		self.w_[0] += self.eta * error
    		cost = 0.5 * (error ** 2)
    
    		return cost
    
    	def net_input(self, X):
    
    		""" Calculate net input """
    
    		return np.dot(X, self.w_[1:]) + self.w_[0]
    
    	def activation(self, X):
    
    		""" Compute linear activation """
    
    		return self.net_input(X)
    
    	def predict(self, X):
    
    		""" Return class label after the unit step """
    
    		return np.where(self.activation(X) >= 0.0, 1, -1)
    	def score(self, X, y):
    		misclassified_data_count = 0
    		for xi, target in zip(X, y):
    			output = self.predict(xi)
    			if(target != output):
    				misclassified_data_count += 1
    		total_data_count = len(X)
    		self.score_ = (total_data_count - misclassified_data_count)/total_data_count
    		return self.score_
        
    # Create the AdalineSGD model
    sgd3 = SGD3(n_iter = 15, eta = 0.01, random_state = 1)
    
    # Train the model
    
    
    # Plot the training errors of both of the models
    df = pd.read_csv('iris.data.txt', header=None)
    y = df.iloc[0:150, 4].values
    y = np.where(y == 'Iris-virginica', 1, -1)
    X = df.iloc[0:150, [0, 2]].values
    sgd3.fit(X, y)
    plt.plot(range(1, len(sgd3.cost_) + 1), sgd3.cost_, marker='o')
    plt.xlabel('Epochs')
    plt.ylabel('error-iris-class3')
    plt.tight_layout()
    plt.show()
    print('classifier three  accuracy-iris',sgd3.score(X,y))
    
    
    dataframe = pd.read_csv('wine-red.txt',header=None,sep=';')
    a = dataframe.iloc[0:1599, 11].values
    a = np.where(y == 7, -1, 1)
    B = dataframe.iloc[0:1599, [0, 2]].values
    sgd3a = SGD3(n_iter = 85, eta = 0.00001, random_state = 1)
    sgd3a.fit(B, a)
    plt.plot(range(1, len(sgd3a.cost_) + 1), sgd3a.cost_, marker='*')
    plt.xlabel('Epochs')
    plt.ylabel('error-wine-class3')
    plt.tight_layout()
    plt.show()
    print('classifier three  accuracy-wine',sgd3a.score(B,a))
    
    

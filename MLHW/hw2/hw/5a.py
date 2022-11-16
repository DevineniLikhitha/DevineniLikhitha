from numpy.random import seed
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#
# Perceptron implementation
#
class Perceptron(object):
     
    def  __init__(self, n_iterations=100, learning_rate=0.01, random_state=1,):
        self.n_iterations = n_iterations
        self.random_state = random_state
        self.learning_rate = learning_rate
 
    '''
    Stochastic Gradient Descent
     
    1. Weights are updated based on each training examples.
    2. Learning of weights can continue for multiple iterations
    3. Learning rate needs to be defined
    '''
    def fit(self, X, y):
        rgen = np.random.RandomState(self.random_state)
        self.coef_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
        for _ in range(self.n_iterations):
            for xi, expected_value in zip(X, y):
                predicted_value = self.predict(xi)
                self.coef_[1:] = self.coef_[1:] + self.learning_rate * (expected_value - predicted_value) * xi
                self.coef_[0] = self.coef_[0] + self.learning_rate * (expected_value - predicted_value) * 1
     
    '''
    Net Input is sum of weighted input signals
    '''
    def net_input(self, X):
            weighted_sum = np.dot(X, self.coef_[1:]) + self.coef_[0]
            return weighted_sum
     
    '''
    Activation function is fed the net input and the unit step function
    is executed to determine the output.
    '''
    def activation_function(self, X):
            weighted_sum = self.net_input(X)
            return np.where(weighted_sum >= 0.0, 1, 0)
     
    '''
    Prediction is made on the basis of output of activation function
    '''
    def predict(self, X):
        return self.activation_function(X)
     
    '''
  accuracy calculation
    '''
    def score(self, X, y):
        misclassified_data_count = 0
        for xi, target in zip(X, y):
            output = self.predict(xi)
            if(target != output):
                misclassified_data_count += 1
        total_data_count = len(X)
        self.score_ = (total_data_count - misclassified_data_count)/total_data_count
        return self.score_
   

df = pd.read_csv('iris.data.txt', header=None)
y = df.iloc[0:100, 4].values # select setosaand versicolor
y = np.where(y == 'Iris-setosa', -1, 1) # Convert the class labels to two integer
X = df.iloc[0:100, [0, 2]].values  # extract sepal length and petal length
ppn= Perceptron(n_iterations=100, learning_rate=0.01)
ppn.fit(X, y)
print('Perceptron accuracy',ppn.score(X,y))



class AdaptiveLinearNeuron(object):
   def __init__(self, rate = 0.01, niter = 10):
      self.rate = rate
      self.niter = niter
      self.errors_ = []

   def fit(self, X, y):
    

      # weights
      self.weight = np.zeros(1 + X.shape[1])

      # Number of misclassifications
      self.errors = []

      # Cost function
      self.cost = []

      for i in range(self.niter):
         output = self.net_input(X)
         errors = y - output
         self.weight[1:] += self.rate * X.T.dot(errors)
         self.weight[0] += self.rate * errors.sum()
         cost = (errors**2).sum() / 2.0
         self.cost.append(cost)
         self.errors_.append(errors) 
      return self

   def net_input(self, X):
      """Calculate net input"""
      return np.dot(X, self.weight[1:]) + self.weight[0]

   def activation(self, X):
      """Compute linear activation"""
      return self.net_input(X)
   

   def predict(self, X):
      """Return class label after unit step"""
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
df = pd.read_csv('iris.data.txt', header=None)
y = df.iloc[0:100, 4].values # select setosaand versicolor
y = np.where(y == 'Iris-setosa', -1, 1) # Convert the class labels to two integer
X = df.iloc[0:100, [0, 2]].values  # extract sepal length and petal length
aln= AdaptiveLinearNeuron(niter=240, rate=0.01)
aln.fit(X, y)
print('Adaline accuracy',aln.score(X,y))

#SGD
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
print('SGD  accuracy',sgd1.score(X,y))



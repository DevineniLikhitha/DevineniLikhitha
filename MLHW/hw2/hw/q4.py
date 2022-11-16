import numpy as np
from numpy.random import seed
import pandas as pd
import matplotlib.pyplot as plt
class Perceptron(object):
    #The constructor of our class.
    def __init__(self, learningRate=0.01, n_iter=50, random_state=1):
        self.learningRate = learningRate
        self.n_iter = n_iter
        self.random_state = random_state
        self.errors_ = []
        
    def fit(self, X, y):
        #for reproducing the same results
        random_generator = np.random.RandomState(self.random_state)
        
        #Step 0 = Get the shape of the input vector X
        #We are adding 1 to the columns for the Bias Term
        x_rows, x_columns = X.shape
        x_columns = x_columns+1
        
        #Step 1 - Initialize all weights to 0 or a small random number  
        #weight[0] = the weight of the Bias Term
        self.weights = random_generator.normal(loc=0.0, scale=0.001, size=x_columns) 
        
        #for how many number of training iterrations where defined
        for _ in range(self.n_iter):
            errors = 0
            for xi, y_actual in zip(X, y):
                #create a prediction for the given sample xi
                y_predicted = self.predict(xi)
                #print(y_actual, y_predicted)
                #calculte the delta
                delta = self.learningRate*(y_actual - y_predicted)
                #update all the weights but the bias
                self.weights[1:] += delta * xi
                #for the bias delta*1 = delta
                self.weights[0] += delta
                #if there is an error. Add to the error count for the batch
                errors += int(delta != 0.0)
            #add the error count of the batch to the errors variable
            self.errors_.append(errors)           
        
        #print(self.errors_)
            
    def Errors(self):
        return self.errors_
    
    def z(self, X):
        #np.dot(X, self.w_[1:]) + self.w_[0]
        z = np.dot(X, self.weights[1:]) + self.weights[0] 
        return z
        
    def predict(self, X):
        #Heaviside function. Returns 1 or 0 
        return np.where(self.z(X) >= 0.0, 1, 0)
df = pd.read_csv('iris.data.txt', header=None)
y = df.iloc[0:100, 4].values # select setosaand versicolor
y = np.where(y == 'Iris-setosa', -1, 1) # Convert the class labels to two integer
X = df.iloc[0:100, [0, 2]].values  # extract sepal length and petal length
ppn= Perceptron(learningRate=0.1, n_iter=10)
ppn.fit(X, y)
plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of misclassifications')
plt.tight_layout()
plt.show()
print('Errors',ppn.errors_)



#Adaline


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


df = pd.read_csv('iris.data.txt', header=None)

y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
X = df.iloc[0:100, [0, 2]].values

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

# learning rate = 0.1
aln1 = AdaptiveLinearNeuron(0.001, 20).fit(X,y)

ax[0].plot(range(1, len(aln1.cost) + 1), np.log10(aln1.cost), marker='o')
ax[0].set_xlabel('Epochs')
ax[0].set_ylabel('log(Sum-squared-error)')
ax[0].set_title('Adaptive Linear Neuron - Learning rate 0.001')

# learning rate = 0.01
aln2 = AdaptiveLinearNeuron(0.1, 15).fit(X,y)

ax[1].plot(range(1, len(aln2.cost) + 1), aln2.cost, marker='o')
ax[1].set_xlabel('Epochs')
ax[1].set_ylabel('Sum-squared-error')
ax[1].set_title('Adaptive Linear Neuron - Learning rate 0.1')
plt.show()

#sum-squared error

ada = AdaptiveLinearNeuron(0.1, 20).fit(X,y)
plt.plot(range(1, len(ada.cost) + 1), ada.cost, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Sum-squared-error')
plt.tight_layout()
plt.show()

print('cost for adaline',ada.cost)



#SGD



class AdalineSGD(object):

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
# Create the AdalineSGD model
adsgd = AdalineSGD(n_iter = 15, eta = 0.01, random_state = 1)

# Train the model
adsgd.fit(X, y)

# Plot the training errors of both of the models
plt.plot(range(1, len(adsgd.cost_) + 1), adsgd.cost_, marker = 'x', color = 'blue')
plt.xlabel('Epochs')
plt.ylabel('Sum-squared-error')
plt.show()
print('cost of SGD',adsgd.cost_)
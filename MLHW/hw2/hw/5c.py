import numpy as np
from numpy.random import seed
import pandas as pd
import matplotlib.pyplot as plt

#testing perceptron with iris data set with one class as negative and other two classes as positive
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
    def score(self, X, y):
        misclassified_data_count = 0
        for xi, target in zip(X, y):
            output = self.predict(xi)
            if(target != output):
                misclassified_data_count += 1
        total_data_count = len(X)
        self.score_ = (total_data_count - misclassified_data_count)/total_data_count
        return self.score_
    
    
    
 #testing with iris data set  
df = pd.read_csv('iris.data.txt', header=None)
y = df.iloc[0:150, 4].values # select setosaand versicolor and virginica
y = np.where(y == 'Iris-versicolor', 1,-1) # Convert the class labels to two integer
X = df.iloc[0:150, [0, 2]].values  # extract sepal length and petal length
ppn= Perceptron(learningRate=0.1, n_iter=10)
ppn.fit(X, y)
plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of misclassifications-iris')
plt.tight_layout()
plt.show()
print('Errors',ppn.errors_)



#testing withanother data set

dataframe = pd.read_csv('pima-indians-diabetes.txt', header=None)
y = dataframe.iloc[0:500, 8].values
y = np.where(y == 0, 1, -1)
X = dataframe.iloc[0:500, [0, 2]].values
ppn1= Perceptron(learningRate=0.1, n_iter=30)
ppn1.fit(X, y)
plt.plot(range(1, len(ppn1.errors_) + 1), ppn1.errors_, marker='+')
plt.xlabel('Epochs')
plt.ylabel('Number of misclassifications-diabetes')
plt.tight_layout()
plt.show()







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
y = np.where(y == 'Iris-setosa', 1, -1)
X = df.iloc[0:100, [0, 2]].values
ada = AdaptiveLinearNeuron(0.00001, 20).fit(X,y)
plt.plot(range(1, len(ada.cost) + 1), ada.cost, marker='o')
plt.xlabel('Epochs')
plt.ylabel('error-iris')
plt.tight_layout()
plt.show()

print('cost for adaline',ada.cost)



dataframe = pd.read_csv('pima-indians-diabetes.txt', header=None)
y = dataframe.iloc[0:500, 8].values
y = np.where(y == 1, 1, -1)
X = dataframe.iloc[0:500, [0, 2]].values
ada1 = AdaptiveLinearNeuron(0.1, 50)
ada1.fit(X,y)
plt.plot(range(1, len(ada1.cost) + 1), ada1.cost, marker='o')
plt.xlabel('Epochs')
plt.ylabel('error-diabetes')
plt.tight_layout()
plt.show()


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


# Plot the training errors of both of the models
df = pd.read_csv('iris.data.txt', header=None)
y = df.iloc[0:150, 4].values
y = np.where(y == 'Iris-virginica', 1, -1)
X = df.iloc[0:150, [0, 2]].values
adsgd.fit(X, y)
plt.plot(range(1, len(adsgd.cost_) + 1), adsgd.cost_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('error-iris')
plt.tight_layout()
plt.show()

#diabetes set

dataframe = pd.read_csv('pima-indians-diabetes.txt', header=None)
y = dataframe.iloc[0:500, 8].values
y = np.where(y == 0, -1, 1)
X = dataframe.iloc[0:500, [0, 2]].values
adsgd1 = AdalineSGD(n_iter = 25, eta = 0.0001, random_state = 1)
adsgd1.fit(X,y)
plt.plot(range(1, len(adsgd1.cost_) + 1), adsgd1.cost_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('error-diabetes')
plt.tight_layout()
plt.show()



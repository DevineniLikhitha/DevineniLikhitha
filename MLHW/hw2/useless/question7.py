import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class onevsrest:
    #classifier 1 
    #Iris-setosa class as 1 and other classes as -1
    class Perceptron1(object):
        #The constructor of our class.
        def __init__(self, learningRate=0.1, n_iter=500, random_state=1):
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
    df = pd.read_csv('iris.data.txt', header=None)
    y = df.iloc[0:150,4].values # select setosaand versicolor
    y = np.where(y == 'Iris-setosa', -1, 1)
    print(y) # Convert the class labels to two integer
    X = df.iloc[0:100, [0, 2]].values  # extract sepal length and petal length
    ppn= Perceptron1(learningRate=0.01,n_iter=500)
    ppn.fit(X, y)
    plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
    plt.xlabel('Epochs')
    plt.ylabel('Number of misclassifications')
    plt.tight_layout()
    plt.show()
    print('Errors',ppn.errors_)
    print('Perceptron one  accuracy',ppn.score(X,y))
    
    #classifier 2
    #Iris-cersicolor as 1 and remaining two as -1
    class Perceptron2(object):
        #The constructor of our class.
        def __init__(self, learningRate=0.1, n_iter=50, random_state=1):
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
    df = pd.read_csv('iris.data.txt', header=None)
    y = df.iloc[0:150,4].values # select setosaand versicolor
    y = np.where(y == 'Iris-versicolor', -1, 1)
    print(y) # Convert the class labels to two integer
    X = df.iloc[0:100, [0, 2]].values  # extract sepal length and petal length
    ppn= Perceptron2(learningRate=0.01,n_iter=50)
    ppn.fit(X, y)
    plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
    plt.xlabel('Epochs')
    plt.ylabel('Number of misclassifications')
    plt.tight_layout()
    plt.show()
    print('Errors',ppn.errors_)
    print('Perceptron two accuracy',ppn.score(X,y))
    
    #classifier 3
    #Iris-virginica as 1 and remaining two as -1
    class Perceptron3(object):
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
    df = pd.read_csv('iris.data.txt', header=None)
    y = df.iloc[0:150,4].values # select setosaand versicolor
    y = np.where(y == 'Iris-virginica', 1, -1)
    print(y) # Convert the class labels to two integer
    X = df.iloc[0:100, [0, 2]].values  # extract sepal length and petal length
    ppn= Perceptron3(learningRate=0.01,n_iter=50)
    ppn.fit(X, y)
    plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
    plt.xlabel('Epochs')
    plt.ylabel('Number of misclassifications')
    plt.tight_layout()
    plt.show()
    print('Errors',ppn.errors_)
    print('Perceptron three accuracy',ppn.score(X,y))
    

    
         
    
    
    
    
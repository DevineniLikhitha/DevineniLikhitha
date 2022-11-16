
import torch

from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader

import torch.nn as nn
import torch.nn.functional as F

import torch.optim as optim

import torchvision
import torchvision.transforms as transforms

import matplotlib.pyplot as plt
import numpy as np



# torchvision.datasets.MNIST outputs a set of PIL images
# We transform them to tensors
transform = transforms.ToTensor()



path = 'C:\\Users\\likhi\\OneDrive\\Desktop\\Course folders\\ML\\hw8' #path need to be change
mnist_dataset = torchvision.datasets.MNIST(root=path, train=True,transform=transform, download=False)
mnist_valid_dataset = torch.utils.data.Subset(mnist_dataset,torch.arange(20000))
mnist_train_dataset = torch.utils.data.Subset(mnist_dataset,torch.arange(20000, len(mnist_dataset)))
mnist_test_dataset = torchvision.datasets.MNIST(root=path, train=False,transform=transform, download=False)
print('number of items in mnist_dataset:', len(mnist_dataset))
print('number of items in mnist_train_dataset:', len(mnist_train_dataset))
print('number of items in mnist_valid_dataset:', len(mnist_valid_dataset))
print('number of items in mnist_test_dataset:', len(mnist_test_dataset))
''' with inputs given in question '''

x = torch.ones((1, 1, 28, 28))
model = nn.Sequential()
model.add_module('conv1',nn.Conv2d(in_channels=1, out_channels=4,kernel_size=3,stride=1 ,padding=0))
model.add_module('relu1', nn.ReLU())
model.add_module('pool1', nn.MaxPool2d(kernel_size=2,stride=2))
print(model(x).shape)
model.add_module('conv2',nn.Conv2d(in_channels=4, out_channels=2,kernel_size=3, stride=3,padding=0))
model.add_module('relu2', nn.ReLU())
model.add_module('pool2', nn.MaxPool2d(kernel_size=4,stride=4))


print(model(x).shape)

model.add_module('flatten', nn.Flatten())

model.add_module('fc1', nn.Linear(2,10))
print(model(x).shape) 

pred = model(mnist_test_dataset.data.unsqueeze(1) / 255.)
is_correct = (torch.argmax(pred, dim=1) == mnist_test_dataset.targets).float()
print(f'Test accuracy: {is_correct.mean():.4f}')





''' With different inputs'''
x = torch.ones((1, 1, 28, 28))
model = nn.Sequential()
model.add_module('conv1',nn.Conv2d(in_channels=1, out_channels=32,kernel_size=5,stride=1 ,padding=2))
model.add_module('relu1', nn.ReLU())
model.add_module('pool1', nn.MaxPool2d(kernel_size=2))
print(model(x).shape)
model.add_module('conv2',nn.Conv2d(in_channels=32, out_channels=64,kernel_size=5 ,padding=2))
model.add_module('relu2', nn.ReLU())
model.add_module('pool2', nn.MaxPool2d(kernel_size=2))
print(model(x).shape)



model.add_module('flatten', nn.Flatten())

model.add_module('fc1', nn.Linear(3136,1024))
print(model(x).shape) 
model.add_module('relu3', nn.ReLU())
model.add_module('dropout', nn.Dropout(p=0.5))
model.add_module('fc2', nn.Linear(1024, 10))
print(model(x).shape) 


pred = model(mnist_test_dataset.data.unsqueeze(1) / 255.)
is_correct = (torch.argmax(pred, dim=1) == mnist_test_dataset.targets).float()
print(f'Test accuracy: {is_correct.mean():.4f}')
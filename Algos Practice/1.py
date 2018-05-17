
# coding: utf-8

# In[37]:


# Akshay Kumar ECS 171


# #
# Construct a 3-layer artificial neural network (ANN) and specifically a feed-forward multilayer
# perceptron to perform multi-class classification. The hidden layer should have 3
# nodes. Split your data into a random set of 70% of the samples as the training set and
# the rest 30% as the testing set. For training, use stochastic gradient descent with backpropagation.
# Please note that you will never train with the testing set; the ANN will only
# take into account the training set for updating the weights. For the most pupular class
# "CYT", provide 2 plots: (I) weight values per iteration for the last layer (3 weights and
# bias), (II) training and test error per iteration. [30pt]

# In[44]:


import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.utils import to_categorical
from keras.optimizers import SGD
from keras.callbacks import Callback

import pandas
import numpy
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt


class per_iteration(Callback):
    def on_train_begin(self,logs={}):
        self.error = []
        self.weight = []
    def on_epoch_end(self,epoch,logs={}):
        self.error.append(logs.get('loss'))
        self.weight.append(self.model.layers[-1].get_weights()[0][0])

# In[39]:


# read in data into a dataframe
df = pandas.read_table('yeast.data.txt',delim_whitespace=True,header=None)
# grab response variables
y = df.loc[:,9].values
# grab names of variables
names = df.loc[:,0].values
# grab input variables
x = df.loc[:,1:8].values

# need to categorize our response variables
label_encoder = LabelEncoder()
encoded_y = label_encoder.fit(y)
y_hot_encoder = encoded_y.transform(y)
final_y = to_categorical(y_hot_encoder,num_classes=10)

# split training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, final_y, train_size=0.7)


# In[48]:


# create artificial neural net
ANN = Sequential()
# 3 hidden nodes
ANN.add(Dense(3,input_dim=8,activation='sigmoid'))
# 10 output nodes (classes)
ANN.add(Dense(10,activation='sigmoid'))
sgd = SGD()
ANN.compile(optimizer=sgd,loss='mean_squared_error')


# In[50]:


record_train = per_iteration()
ANN.fit(x_train,y_train,epochs=25,batch_size=1,validation_data=(x_test,y_test),callbacks=[record_train])


# In[51]:


plt.plot(record_train.weight[0])
plt.ylabel('weight value')
plt.show()
plt.plot(record_train.error)
plt.ylabel('training and test error')
plt.show()


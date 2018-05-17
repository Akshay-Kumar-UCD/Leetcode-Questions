
# coding: utf-8

# In[1]:


#Increase the number of hidden layers from 1 to 2 and then to 3. Then increase the number
#of hidden nodes per layer from 3 to 6, then to 9 and finally to 12. Create a 3x4 matrix
#with the number of hidden layers as rows and the number of hidden nodes per layer as
#columns, with each element (cell) of the matrix representing the testing set error for that
#specific combination of layers/nodes. What is the optimal configuration? What you find
#the relationship between these attributes (number of layers, number of nodes) and the
#generalization error (i.e. error in testing data) to be? [25pt]


# In[2]:


# Akshay Kumar ECS 171


# In[38]:


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
import numpy


# In[33]:


class per_iteration(Callback):
    def on_train_begin(self,logs={}):
        self.error = []
        self.weight = []
    def on_epoch_end(self,epoch,logs={}):
        self.error.append(logs.get('loss'))
        self.weight.append(self.model.layers[-1].get_weights()[0][0])


# In[18]:


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



# In[20]:


one = Sequential()
# 3 hidden nodes
one.add(Dense(3,input_dim=8,activation='sigmoid'))
# 10 output nodes (classes)
one.add(Dense(10,activation='sigmoid'))
sgd = SGD()
one.compile(optimizer=sgd,loss='mean_squared_error')


# In[21]:


two = Sequential()
# 6 hidden nodes
two.add(Dense(6,input_dim=8,activation='sigmoid'))
# 10 output nodes (classes)
two.add(Dense(10,activation='sigmoid'))
sgd = SGD()
two.compile(optimizer=sgd,loss='mean_squared_error')


# In[22]:


three = Sequential()
# 9 hidden nodes
three.add(Dense(9,input_dim=8,activation='sigmoid'))
# 10 output nodes (classes)
three.add(Dense(10,activation='sigmoid'))
sgd = SGD()
three.compile(optimizer=sgd,loss='mean_squared_error')


# In[23]:


four = Sequential()
# 12 hidden nodes
four.add(Dense(12,input_dim=8,activation='sigmoid'))
# 10 output nodes (classes)
four.add(Dense(10,activation='sigmoid'))
sgd = SGD()
four.compile(optimizer=sgd,loss='mean_squared_error')


# In[24]:


five = Sequential()
# 3 hidden nodes
five.add(Dense(3,input_dim=8,activation='sigmoid'))
five.add(Dense(3,input_dim=8,activation='sigmoid'))
# 10 output nodes (classes)
five.add(Dense(10,activation='sigmoid'))
sgd = SGD()
five.compile(optimizer=sgd,loss='mean_squared_error')


# In[25]:


six = Sequential()
# 6 hidden nodes
six.add(Dense(6,input_dim=8,activation='sigmoid'))
six.add(Dense(6,input_dim=8,activation='sigmoid'))
# 10 output nodes (classes)
six.add(Dense(10,activation='sigmoid'))
sgd = SGD()
six.compile(optimizer=sgd,loss='mean_squared_error')


# In[26]:


seven = Sequential()
# 9 hidden nodes
seven.add(Dense(9,input_dim=8,activation='sigmoid'))
seven.add(Dense(9,input_dim=8,activation='sigmoid'))
# 10 output nodes (classes)
seven.add(Dense(10,activation='sigmoid'))
sgd = SGD()
seven.compile(optimizer=sgd,loss='mean_squared_error')


# In[27]:


eight = Sequential()
# 12 hidden nodes
eight.add(Dense(12,input_dim=8,activation='sigmoid'))
eight.add(Dense(12,input_dim=8,activation='sigmoid'))
# 10 output nodes (classes)
eight.add(Dense(10,activation='sigmoid'))
sgd = SGD()
eight.compile(optimizer=sgd,loss='mean_squared_error')


# In[28]:


nine = Sequential()
# 3 hidden nodes
nine.add(Dense(3,input_dim=8,activation='sigmoid'))
nine.add(Dense(3,input_dim=8,activation='sigmoid'))
nine.add(Dense(3,input_dim=8,activation='sigmoid'))
# 10 output nodes (classes)
nine.add(Dense(10,activation='sigmoid'))
sgd = SGD()
nine.compile(optimizer=sgd,loss='mean_squared_error')


# In[29]:


ten = Sequential()
# 6 hidden nodes
ten.add(Dense(6,input_dim=8,activation='sigmoid'))
ten.add(Dense(6,input_dim=8,activation='sigmoid'))
ten.add(Dense(6,input_dim=8,activation='sigmoid'))
# 10 output nodes (classes)
ten.add(Dense(10,activation='sigmoid'))
sgd = SGD()
ten.compile(optimizer=sgd,loss='mean_squared_error')


# In[30]:


eleven = Sequential()
# 9 hidden nodes
eleven.add(Dense(9,input_dim=8,activation='sigmoid'))
eleven.add(Dense(9,input_dim=8,activation='sigmoid'))
eleven.add(Dense(9,input_dim=8,activation='sigmoid'))
# 10 output nodes (classes)
eleven.add(Dense(10,activation='sigmoid'))
sgd = SGD()
eleven.compile(optimizer=sgd,loss='mean_squared_error')


# In[31]:


twelve = Sequential()
# 3 hidden nodes
twelve.add(Dense(12,input_dim=8,activation='sigmoid'))
twelve.add(Dense(12,input_dim=8,activation='sigmoid'))
twelve.add(Dense(12,input_dim=8,activation='sigmoid'))
# 10 output nodes (classes)
twelve.add(Dense(10,activation='sigmoid'))
sgd = SGD()
twelve.compile(optimizer=sgd,loss='mean_squared_error')


# In[37]:


error_list = []

record_train = per_iteration()
one.fit(x_train,y_train,epochs=25,batch_size=1,validation_data=(x_test,y_test),callbacks=[record_train])
error_list.append(record_train.error[0])

record_train = per_iteration()
two.fit(x_train,y_train,epochs=25,batch_size=1,validation_data=(x_test,y_test),callbacks=[record_train])
error_list.append(record_train.error[0])

record_train = per_iteration()
three.fit(x_train,y_train,epochs=25,batch_size=1,validation_data=(x_test,y_test),callbacks=[record_train])
error_list.append(record_train.error[0])

record_train = per_iteration()
four.fit(x_train,y_train,epochs=25,batch_size=1,validation_data=(x_test,y_test),callbacks=[record_train])
error_list.append(record_train.error[0])

record_train = per_iteration()
five.fit(x_train,y_train,epochs=25,batch_size=1,validation_data=(x_test,y_test),callbacks=[record_train])
error_list.append(record_train.error[0])

record_train = per_iteration()
six.fit(x_train,y_train,epochs=25,batch_size=1,validation_data=(x_test,y_test),callbacks=[record_train])
error_list.append(record_train.error[0])

record_train = per_iteration()
seven.fit(x_train,y_train,epochs=25,batch_size=1,validation_data=(x_test,y_test),callbacks=[record_train])
error_list.append(record_train.error[0])

record_train = per_iteration()
eight.fit(x_train,y_train,epochs=25,batch_size=1,validation_data=(x_test,y_test),callbacks=[record_train])
error_list.append(record_train.error[0])

record_train = per_iteration()
nine.fit(x_train,y_train,epochs=25,batch_size=1,validation_data=(x_test,y_test),callbacks=[record_train])
error_list.append(record_train.error[0])

record_train = per_iteration()
ten.fit(x_train,y_train,epochs=25,batch_size=1,validation_data=(x_test,y_test),callbacks=[record_train])
error_list.append(record_train.error[0])

record_train = per_iteration()
eleven.fit(x_train,y_train,epochs=25,batch_size=1,validation_data=(x_test,y_test),callbacks=[record_train])
error_list.append(record_train.error[0])

record_train = per_iteration()
twelve.fit(x_train,y_train,epochs=25,batch_size=1,validation_data=(x_test,y_test),callbacks=[record_train])
error_list.append(record_train.error[0])


# In[39]:


matrix = numpy.array(error_list)
matrix = matrix.reshape(3,4)
print(matrix)



# coding: utf-8

# In[1]:


#Which class does the following sample belong to?[5pt]
#Unknown Sample 0.49 0.51 0.52 0.23 0.55 0.03 0.52 0.39


# In[2]:


# Akshay Kumar ECS 171


# In[3]:



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


# In[39]:


unknown = numpy.array([0.49, 0.51, 0.52, 0.23, 0.55, 0.03, 0.52, 0.39])
unknown = numpy.reshape(unknown,(1,8))
known = ANN.predict(unknown,batch_size=1)
print(known)


# In[40]:


# CYT, which shows up first alphabetically 


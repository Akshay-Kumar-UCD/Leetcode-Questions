import multiprocessing as mp
from sklearn.datasets import load_svmlight_file
import numpy as np
import time

traindata = load_svmlight_file("a9a.subset.train")
testdata = load_svmlight_file("a9a.subset.test")
Xtrain = traindata[0].todense()
ytrain = traindata[1]
Xtest = testdata[0].todense()
ytest = testdata[1]

def go_nn(Xtrain, ytrain, Xtest, ytest):
    correct =0
    for i in range(Xtest.shape[0]): ## For all testing instances
        nowXtest = Xtest[i,:]
        ### Find the index of nearest neighbor in training data
        dis_smallest = np.linalg.norm(Xtrain[0,:]-nowXtest) 
        idx = 0
        for j in range(1, Xtrain.shape[0]):
            dis = np.linalg.norm(nowXtest-Xtrain[j,:])
            if dis < dis_smallest:
                dis_smallest = dis
                idx = j
        ### Now idx is the index for the nearest neighbor
        
        ## check whether the predicted label matches the true label
        if ytest[i] == ytrain[idx]:  
            correct += 1
    acc = correct/float(Xtest.shape[0])
    return acc

# the following function allows for inputting multiple arguments into the map function 
# it comes from https://stackoverflow.com/questions/5442910/python-multiprocessing-pool-map-for-multiple-arguments
def more_args_map(i):
	return go_nn(*i)

start_time = time.time()

# the idea to split the test data comes from Piazza, and is done so in order to split the work the four processes need to do 
list_ytest = np.split(ytest,4)
ytest0 = list_ytest[0]
ytest1 = list_ytest[1]
ytest2 = list_ytest[2]
ytest3 = list_ytest[3]
list_Xtest = np.split(Xtest,4)
Xtest0 = list_Xtest[0]
Xtest1 = list_Xtest[1]
Xtest2 = list_Xtest[2]
Xtest3 = list_Xtest[3]

# the use of Pool and map comes from Clark's GitHub, specifically Week 9, example.py
pool = mp.Pool(processes=4)
list_acc = pool.map(more_args_map, [(Xtrain, ytrain, Xtest0, ytest0),
			(Xtrain, ytrain, Xtest1, ytest1),(Xtrain, ytrain, Xtest2, ytest2),
			(Xtrain, ytrain, Xtest3, ytest3)])
acc = sum(list_acc) / float(len(list_acc))
print("Accuracy %lf Time %lf secs.\n"%(acc, time.time()-start_time))
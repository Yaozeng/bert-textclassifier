import pandas as pd
train_set=pd.read_csv("data/data_train.csv",header=None)
train_set.info()
print(train_set.values[0][2])
print(len(train_set.values[0][2]))
#print(train_set[train_set[2].str.len()>=440])

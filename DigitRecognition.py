import numpy as np
import matplotlib.pyplot as pt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('digitdata/train.csv').as_matrix()
# print(data)

clf = DecisionTreeClassifier()

xtrain = data[0:21000, 1:]
train_lable = data[0:21000, 0]

clf.fit(xtrain, train_lable)

xtest = data[21000:, 1:]
actual_label = data[21000:, 0]

d = xtest[3]
d.shape = (28, 28)
pt.imshow(255-d, cmap='gray')
print(clf.predict([xtest[3]]))
pt.show()


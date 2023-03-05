import unittest

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from PForecaster import prediction, NN_model
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from xgboost import XGBClassifier
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

from PermutationForecaster import PermutationForecaster

df = pd.read_csv("/Users/ara_vartomian/Downloads/JEPI (1).csv")
pf = PermutationForecaster(df['Close'])
#b = pf.indexer(window_size=5)
target = pf.bin_maker(threshold=7,window_size=15)
a = pf.targetDeleter(window_size=15)
df1 = pd.DataFrame(a)
# print(df1)
#df1['target'] = target
X_train, X_test, y_train, y_test = train_test_split(df1, target, test_size=.20, random_state=42)
# y_test1 = y_test
# X_train, X_test, y_train, y_test = np.array(X_train), np.array(X_test),np.array(y_train), np.array(y_test)
# #print(X_train)
# pred = NN_model(X_train, X_test,y_train, y_test)
# #acc1 = accuracy_score(y_test, pred)
# acc = accuracy_score(y_test, pred)
# print(pred)
pred = prediction(X_train,y_train, X_test)
pred_train = prediction(X_train, y_train, X_train)
acc = accuracy_score(y_train, pred_train)
print(acc)
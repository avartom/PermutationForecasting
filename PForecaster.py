from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from xgboost import XGBClassifier
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def prediction(X_train, y_train, X_test):
  xgbclassifier = XGBClassifier(max_depth=10, n_estimators=1000, random_state=42)
  xgbclassifier.fit(X_train, y_train)
  y_pred = xgbclassifier.predict(X_test)
  return y_pred

def NN_model(X_train, X_test, y_train,y_test):
  model = Sequential()
  model.add(Dense(64, activation="relu"))
  model.add(Dense(64, activation="relu"))
  model.add(Dense(64, activation="relu"))
  model.add(Dense(1, activation='sigmoid'))
  model.compile(loss='binary_crossentropy', optimizer='adam', metrics =["accuracy"])
  model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=2)
  _, accuracy = model.evaluate(X_test, y_test)
  return accuracy

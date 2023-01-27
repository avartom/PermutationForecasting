from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from xgboost import XGBClassifier
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def prediction(n,test_size=11):
  xgbclassifier = XGBClassifier(max_depth=10, n_estimators=500, random_state=42)
  xgbclassifier.fit(train_test(n)[0], train_test(n)[1])
  y_pred = xgbclassifier.predict(train_test(n)[2])
  return y_pred[0]


list_p = []
for i in range(10):
  y = prediction(i)
  list_p.append(y)
list_t = train_test(0)[3]

acc_score = accuracy_score(list_t,list_p)

model = Sequential()
model.add(Dense(64, activation="relu"))
model.add(Dense(64, activation="relu"))
model.add(Dense(64, activation="relu"))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics =["accuracy"])
model.fit(X_train, y_train, epochs=100, batch_size=1, verbose=2)

y_test = clean_df["target"][234:244]
X_test = clean_df[['Sprice0',	'Sprice1',	'Sprice2','Sprice3', 'Sprice4']].iloc[234:244]
_, accuracy = model.evaluate(X_test, y_test)


X_test1 = clean_df[['Sprice0',	'Sprice1',	'Sprice2','Sprice3', 'Sprice4']].iloc[244:245]
prediction = model.predict(X_test1)
prediction = (prediction > 0.5).astype(int)
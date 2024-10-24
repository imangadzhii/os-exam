import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,mean_squared_error,classification_report, confusion_matrix
import matplotlib.pyplot as plt

data = pd.read_csv("3cweather.csv")
# print(data.head())
# print(data.shape)

x = data[['temperature','humidity']]
y = data['weather1']

model = DecisionTreeClassifier()
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.245)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
acc = accuracy_score(y_test,y_pred)
# print(acc*100)
print(classification_report(y_test,y_pred) )
print(confusion_matrix(y_test,y_pred))
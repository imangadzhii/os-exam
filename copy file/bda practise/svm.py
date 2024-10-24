import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error,accuracy_score
import matplotlib.pyplot as plt

model = SVR(kernel='linear')

data = pd.read_csv('org weather.csv')
x = data[['humidity']]
y = data.temperature
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.245)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print(mean_squared_error(y_test,y_pred))

plt.scatter(x_test,y_test,color = 'red')
plt.plot(x_test,y_pred,color = 'blue')
plt.title('Humidity vs Temperature')
plt.xlabel('Humidity')
plt.ylabel('Temperature')
plt.show()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

data = pd.read_csv('org weather.csv')
# data.head()
x = data[['humidity']]
y = data['temperature']
# for i,j in zip(x,y):
#   print(f"Humidity: {i} ;; Temperature: {j}")
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.245)
lin = LinearRegression()

lin.fit(x_train,y_train)
pred_value = lin.predict(x_test)
mse= mean_squared_error(y_test, pred_value)
print(mse)

plt.scatter(x_test,y_test,color = 'red')
plt.plot(x_test,pred_value,color = 'blue')
plt.title('Humidity vs Temperature')
plt.xlabel('Humidity')
plt.ylabel('Temperature')
plt.show()
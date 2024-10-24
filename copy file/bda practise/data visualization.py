import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('org weather.csv')
x = data['temperature']
y = data['humidity']

plt.scatter(x,y,color='green')
plt.title('Temperature vs Humidity')
plt.legend()
plt.show()

plt.hist(x,bins=20)
plt.title('Histogram for Temperature')
plt.legend()
plt.show()

plt.hist(y,bins=20)
plt.title('Histogram for Humidity')
plt.legend()
plt.show()

sns.pairplot(data)
plt.show()
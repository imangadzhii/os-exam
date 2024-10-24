import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('new weather.csv')
print(data.sample(15))

x = data[['temperature', 'humidity']]
scaler = StandardScaler()

x_scaled = scaler.fit_transform(x)

inertia = []
for n in range(1,11):
    kmean = KMeans(n_clusters= n, random_state=42)
    kmean.fit(x_scaled)
    inertia.append(kmean.inertia_)
plt.scatter(range(1,11),inertia)
plt.show()

n = 3
k = KMeans(n_clusters=n,random_state=49)
k.fit(x_scaled)
lab = k.labels_
centers = k.cluster_centers_

data['clusters'] = lab

for x in range(n):
    cluster_data = data[data['clusters']==x]
    plt.scatter(cluster_data['temperature'], cluster_data['humidity'])
plt.show()
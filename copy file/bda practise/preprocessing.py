import random

def generating_weather_data(num):
  dataset = []
  for _ in range(num):
    temperature = random.randint(-10,39)
    humidity = random.randint(0, 100)
    dataset.append((temperature, humidity))
  return dataset

def pre_processing(data):
  preprocessed_data = []
  for t,h in data:
    if t >=0:
      nh = h/100.00
      preprocessed_data.append((t,nh))
  return preprocessed_data

if __name__ == "__main__":
  data = generating_weather_data(1000)
  preprocessed_data = pre_processing(data)
  for i,j in preprocessed_data:
    print(f"Temperature :{i} ;; Humidity: {j}")

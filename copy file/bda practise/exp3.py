import random
from multiprocessing import Pool

def generating_weather_data(num):
  dataset = []
  for _ in range(num):
    temperature = random.randint(-10,39)
    humidity = random.randint(0, 100)
    dataset.append((temperature, humidity))
  return dataset

def map_temperature(data):
  temperature,humidity = data
  return temperature, 1

def map_humidity(data):
  temperature,humidity = data
  return humidity, 1

def reduce_counts(data):
  key, counts = data
  return key,sum(counts)

def map_reduce(data,mapper,reducer):
  mapped_data = [mapper(item) for item in data]
  grouped_data = {}
  for key, value in mapped_data:
    grouped_data.setdefault(key,[]).append(value)
    reduced_data =[reducer((key, value)) for key,value in grouped_data.items()]
  return reduced_data

if __name__ == "__main__":
  data = generating_weather_data(1000)
  temperature_counts = map_reduce(data,map_temperature,reduce_counts)
  print("Temperature counts:", temperature_counts)
  humidity_counts = map_reduce(data,map_humidity,reduce_counts)
  print("Humidity counts:", humidity_counts)



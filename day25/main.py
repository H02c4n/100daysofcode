# import csv


# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         temperatures.append(row[1])
#     temperatures = temperatures[1:]
#     print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
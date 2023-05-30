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
print(type(data))
print(data["temp"])
print(type(data["temp"]))


data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

average = sum(temp_list) / len(temp_list)
print(average)

print(data["temp"].mean())

maxTemp = data["temp"].max()
print(maxTemp)
print(data["condition"])
print(data.condition)

# Get data in Row

monday = data[data.day =="Monday"]
print(monday)

print(data[data.temp == data.temp.max()])

print(monday.condition)

monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

#create dataFrame from scratch

data_dict = {
    "students": ["Any", "James", "Angela"],
    "scores": [76, 56, 65]
}

new_data = pandas.DataFrame(data_dict)
print(f"New_data : {new_data}")

new_csv = new_data.to_csv("new_data.csv")
print(new_csv)
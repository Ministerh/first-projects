#with open("./Data Analysis/weather_data.csv")  as weather:
#    data = weather.readlines()
#    print(data)
# import csv
# with open("./Data Analysis/weather_data.csv")  as weather:
#     data = csv.reader(weather)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))

#     print(temperature)

import pandas
#data = pandas.read_csv("./Data Analysis/weather_data.csv")
#print(type(data))
#print(type(data["temp"]))
#this is data refer frame
#data_dict = data.to_dict()
#print(data_dict)
#temp_list = data["temp"].to_list()
#$print(temp_list)
#to get  the average  which is also the mean
#print(data["temp"].mean())
#print(data["temp"].max())
#you can also get a heading using attribute
#print(data.condition)
"or you can say "
#print(data["condition"])

#get data in a row
#print(data[data.condition == "Sunny"])
#print(data[data.temp == data.temp.max()])
       
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

#create a dataframe from scrtach
#data_dict = {
#    "students": ["Amy", "James", "Minister"],
#    "scores": [76, 56, 65]
#}
#using pandas convert to frame
#data = pandas.DataFrame(data_dict)
#convert this into csv file by using pandas method
#data.to_csv("data_structure.csv")
data = pandas.read_csv("./Data Analysis/2018_Central_Park_Squirrel_Census_Data.csv")

#print(data[data.Primary_Fur_Color == "Gray"])
color_list = data.Primary_Fur_Color.to_list()
cinnamon_squirrel =len(data[data.Primary_Fur_Color == "Cinnamon"])
#eprint(cinnamon_squirrel)
gray_squirrel = len(data[data.Primary_Fur_Color == "Gray"])
#print(gray_squirrel)
black_squirrel = len(data[data.Primary_Fur_Color == "Black"])
#print(black_squirrel)

data_dict = {
    "squirrel fur color": ["cinnamon", "gray", "black"],
    "squirrel_count": [cinnamon_squirrel, gray_squirrel, black_squirrel]
}
data =  pandas.DataFrame(data_dict)
data.to_csv("./Data Analysis/squirrel_count.csv")


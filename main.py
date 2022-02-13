# # with open("weather_data.csv", 'r') as w:
# #     data=[]
# #     # print(w.readlines())
# #     # data=w.readlines()
# #     data.append(w.readlines())
# #     print(data)
#
# import csv
#
# with open("weather_data.csv") as we:
#     data = csv.reader(we)
#     temp=[]
#     for lines in data:
#         if lines[1]!="temp":
#             temp.append(int(lines[1]))
#     print(temp)
#
import pandas as pd
data=pd.read_csv("weather_data.csv")
# temp=data["temp"].tolist()
# print(type(data))
# c=0
# s=0
# for value in temp:
#     c+=1
#     s=s+value
#
# avg=s/c
# print(avg)
# print (data["temp"].max()  )
# max=data["temp"].max()
# print(data[data.temp==max])
monday=data[data.day == "Sunny"]
print(((monday.temp) * 9/5) + 32 )

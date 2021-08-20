"""
comvert
text to csv
learn pandas
"""
import pandas

my_data = pandas.read_csv(
 "D:\project-code\small_project\python\csv file\points.txt")
#print(my_data)
my_data.to_csv("D:\project-code\small_project\python\csv file\points.csv",index= None)
my_data = pandas.read_csv(
    "D:\project-code\small_project\python\csv file\points.txt")

# #print(my_data)
# my_data.to_csv(
#     "D:\project-code\small_project\python\csv file\points.csv", index=None)
# my_data.columns = ["Name","Points"]
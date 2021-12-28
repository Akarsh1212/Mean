import csv
with open ("class2.csv" , newline = '') as f :
    reader = csv.reader(f)
    file_Data = list(reader)
file_Data.pop(0)
total_Marks = 0
total_Entry = len(file_Data)
for marks in file_Data:
    total_Marks += float(marks[1])
mean = total_Marks/total_Entry
print(f"Mean is : {mean}")
import pandas as pd
import plotly.express as ps
df = pd.read_csv("class2.csv")
fig = ps.scatter(df,x = "Student Number",y = "Marks")
fig.update_layout(shapes = [
    dict(
        type = 'line',
        y0 = mean, y1 = mean,
        x0 = 0, x1 = total_Entry
    )
])
fig.update_yaxes(rangemode = "tozero")
fig.show()
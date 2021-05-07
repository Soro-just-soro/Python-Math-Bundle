import csv
import plotly.express as px
with open("./Student Marks vs Days Present.csv") as csvFile:
    df=csv.DictReader(csvFile)
    fig=px.scatter(df,x="Days Present",y="Marks In Percentage")
    fig.show()
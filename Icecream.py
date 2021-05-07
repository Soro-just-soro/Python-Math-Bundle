import csv
import plotly.express as px
with open("./Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv") as csvFile:
    df=csv.DictReader(csvFile)
    fig=px.scatter(df,x="Temperature",y="Ice-cream Sales")
    fig.show()
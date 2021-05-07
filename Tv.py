import csv
import numpy as np
def getDataSource(dataPath):
    sizeOfTV=[]
    timeSpent=[]
    with open(dataPath)as csvFile:
        csvReader=csv.DictReader(csvFile)
        for row in csvReader:
            sizeOfTV.append(float(row["Size of TV"]))
            timeSpent.append(float(row["time spent watching TV"]))
    return {"x":sizeOfTV,"y":timeSpent}
def FindCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print(correlation[0,1])
def main():
    dataPath="./Size of TV,_Average time spent watching TV in a week (hours).csv"
    dataSource=getDataSource(dataPath)
    FindCorrelation(dataSource)
main()
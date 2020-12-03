import csv

with open('TableOutput.csv','rt')as f:
    data = csv.reader(f)
    for row in data:
        print(row)
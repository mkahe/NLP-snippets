import csv
import os
from statistics import mean

with open(os.getcwd() + '/Test/grades.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        name = row[0]
        grades = list(map(float, row[1:10])) 
        GPA = mean(grades)
        print('Name: %s, GPA: %2.2f' %(name, GPA)) # how to format the floats inline
# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
csvpath = os.path.join("..", "Resources", "netflix_ratings.csv")

found = False

with open(csvpath) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')

for row in csvReader:
    if row[0] == video:
        print(row[0] + "has a rating of " + row[7] + "and came out in year " + row[6])
    found = True
    break

if found is False:
        print("movie Not Found")


import os
import csv

cereal_csv = os.path.join("..", "Resources", "cereal.csv")

# Open and read csv
with open(cereal_csv) as csv_file:
    csvReader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_file)
    
    for row in csvReader:
        if float(row[7]) >= 5:
            print (row)
        


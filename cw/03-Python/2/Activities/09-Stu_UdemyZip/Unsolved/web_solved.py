import os
import csv

udemy_csv = os.path.join("..", "Resources", "web_starter.csv")
    

# Lists to store data
title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []

# Use encoding for Windows
# with open(udemy_csv, newline='', encoding='utf-8') as csvfile:
# OR below one for MAC
with open(udemy_csv, newline='') as csvfile:
    csvReader = csv.reader(csvfile, delimiters=',')
    for row in csvReader:
        title.append(row[1])
        price.append(row[4])
        subscribers.append(row[5])
        reviews.append(row[6])
        review_percent.append(int(row[6])/int(row[5]))
        length.append(row[9].split(" ")[0])

new_list = zip (title,price,subscribers,reviews,review_percent,length)

print(list(new_list))
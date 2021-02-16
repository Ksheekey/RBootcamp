import os
import csv

# Path to collect data from the Resources folder
wrestling_csv = os.path.join('..', 'Resources', 'WWE-Data-2016.csv')

def print_percentages(wrestler_data):
# Define the function and have it accept the 'wrestlerData' as its sole parameter
    name = str(wrestler_data[0])
    wins = int(wrestler_data[1])
    losses = int(wrestler_data[2])
    draws = int(wrestler_data[3])

# Find the total number of matches wrestled
    matches = wins + losses + draws
    print (matches)

# Find the percentage of matches won
    win_percentage = (wins / matches) * 100

# Find the percentage of matches lost
    loss_percentage = (losses / matches) * 100

# Find the percentage of matches drawn
    draw_percentage = (draws / matches) * 100

    if loss_percentage > 50:
        wrest_type = "jobber"
    else:
        wrest_type = "superstar"

# Print out the wrestler's name and their percentage stats
    print (f'Wrestler {name} is a {wrest_type}')
    print (f'Winning percentage is {win_percentage}')
    print (f'Losing percentage is {loss_percentage}')
    print (f'Draw percentage is {draw_percentage}')

# Read in the CSV file
with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if(name_to_check == row[0]):
            print_percentages(row)

# Create a variable called 'name' that holds a string
name = "Kevin"

# Create a variable called 'country' that holds a string
country = "USA"

# Create a variable called 'age' that holds an integer
age = 33

# Create a variable called 'hourly_wage' that holds an integer
hourly_wage = 25

# Calculate the daily wage for the user
daily_wage = 8*hourly_wage

# Create a variable called 'satisfied' that holds a boolean
satisfied = False

# Print out "Hello <name>!"
print("Hello " + name)

# Print out what country the user entered
print(name + " has entered " + country)

# Print out the user's age
print(name + " is " + str(age) + " years old")

# With an f-string, print out the daily wage that was calculated
print(f"{name} makes ${daily_wage} per day")

# With an f-string, print out whether the users were satisfied
print(f"is {name} satisfied with make ${daily_wage} poer day? {satisfied}")

fish = "halibut"

# Loop through each letter in the string
# and push to an array
letters = []

for letter in fish:
    letters.append(letter)

print(letters)

# List comprehensions provide concise syntax for creating lists

letters = [letter for letter in fish]
print(letters)

# We can manipulate each element as we go
capital_letters = []
proper_case = []
i=0
for letter in fish:
    if i==0:
        proper_case.append(letter.upper())
    else: 
        proper_case.append(letter.lower())
    i=i+1
print(proper_case)
#enumerate
i=0
proper_case = [letter.upper() if i==0 else letter.lower() for letter in fish]

print(proper_case)

# List Comprehension for the above

print(capital_letters)

# We can also add conditional logic (if statements) to a list comprehension
july_temperatures = [87, 85, 92, 79, 106]
hot_days = []
for temperature in july_temperatures:
    if temperature > 90:
        hot_days.append(temperature)
print(hot_days)

# List Comprehension with conditional
hot_days = [temperature for temperature in july_temperatures if temperature > 90]
print(hot_days)

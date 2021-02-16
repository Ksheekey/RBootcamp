# Dictionary full of info
my_info = {"name": "Kevin",
            "age": 33,
            "Hobbies": ["biking", "Soccer"],
            "Sleep": {"sun":9, "Mon":10}
            }

# Print out results are stored in the dictionary
print(f'Hi my name is {my_info["name"]} and i am {my_info["age"]} years old')
print(f'My Hobbies are {my_info["Hobbies"]} but my favore is {my_info["Hobbies"][0]}')
print(f'On Monday i wake up at {my_info["Sleep"]["Mon"]}')

#if you want to print the keys from your dictionary
print (my_info.keys())
# Initial variable to track shopping status
shopping = 'y'

# List to track pie purchases
pie_purchases = [0,0,0,0,0,0,0,0,0,0]

# Pie List
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

# Display initial message
print("Welcome to the House of Pies! Here are our pies:")

# While we are still shopping...
# Loop starts here

while shopping == "y":
    int_pos = int(input("Choose the pie you would like : "))
    pie_purchases[int_pos] = pie_purchases[int_pos] + 1
    shopping = input("shop more? y or n ")




# Loop end here
# Once the pie list is complete
print("------------------------------------------------------------------------")
print("You purchased a total of " + str(len(pie_purchases)) + ".")

i = 0
for pie in pie_list:
    print(str(pie_purchases)[i] + pie_list[i])
    i = i + 1
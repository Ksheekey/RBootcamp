# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []

# Print out options
i = 0
for candy in candy_list:
    print('[' + str(i) + ']' + " " + candy)
    i=i+1

need_more="yes"
while need_more == "yes" and len(candy_cart) < 5:
    selected_item = int(input("Choose the Number : "))
    candy_cart.append(candy_list[selected_item])
    need_more=input("Do you need more? ")

print (candy_cart)

# 1. naem x and y - see if 2xX is greater then 10 print, else print
x = 5
y = 10
if (2*x > 10):
    print ("#1 works!")
else:
    print("#1 Untrue..")


# 2. rename x and y - see if the length of the word dog is less then x print, else print
x = 5
y = 10
if len("dog") < x:
    print("#2 works!")
else:
    print("#2 Untrue..")

# 3. rename x and y - see if x to the power of 3  is greater then or equal to y and y to the power of 2 is less then 26 print, else print
x = 3
y = 5
if (x ** 3 >= y) and (y ** 2 < 26):
    print("#3 Works!")
else:
    print("#3 Untrue..")

# 4. - find dan in the group!
name = "Dan"
group_one = ("Tony", "Fred", "Jolene")
group_two = ("Dan", "Steve", "Mary", "Peggy")
group_three = ("Lisa", "Joe", "Kevin", "Tonya")
if name in group_one:
    print(name + " is in group one")
elif name in group_two:
    print(name + " is in group two")
elif name in group_three:
    print(name + " is in group three")
else:
    print("Dan is not coming")

# 5.
height = 66
age = 16
adult_permission = True

if (height > 70) and (age >= 18):
    print("Can ride all the roller coasters")
elif (height > 65) and (age >= 18):
    print("Can ride moderate roller coasters")
elif (height > 60) and (age >= 18):
    print("Can ride light roller coasters")
elif ((height > 50) and (age >= 18)) or ((adult_permission) and (height > 50)):
    print("Can ride bumper cars")
else:
    print("Stick to lazy river")

# Create a variable and set it as an ListmyList = ["Jacob", 25, "Ahmed", 80]
myList = ["Kevin", 33, "Chrissy", 35]
print(myList)

# Adds an element onto the end of a List
myList.append("Joey")
myList.append(39)
myList.append("Sharon")
myList.append(40)
print(myList)

# Returns the index of the first object with a matching value
print(myList.index("Joey"))

# Changes a specified element within an List at the given index
myList[2]="Christine"
print(myList)

# Returns the length of the List
print(len(myList))

# Removes a specified object from an List
myList.remove("Joey")
print(myList)

# Removes the object at the index specified
myList.pop(4)
print(myList)

# Creates a tuple, a sequence of immutable Python objects that cannot be changed


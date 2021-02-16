# Collects the user's input for the prompt "What is your name?"
name = input("What is your name? ")

# Collects the user's input for the prompt "How old are you?" and converts the string to an integer.
age = int(input("How old are you? "))

# Collects the user's input for the prompt "Is input truthy?" and converts it to a boolean. Note that non-zero,
#   non-empty objects are truth-y.
ToF = bool(input("Is the input true? (If no just hit enter): "))

# Creates three print statements that to respond with the output.
print("-------------------------------------------------")
print("My name is " + name)
print("I am " + str(age) + ", but I will be " + str(age + 1) + " next year")
print("The above informationg is " + str(ToF))












#name = input("What is your name? ")
#age = int(input("How old are you? "))
#trueOrFalse = bool(input("Is the input truthy? "))
#print("My name is " + str(name))
#print("I will be " + str(age + 1) + " next year.")
#print("The input was converted to " + str(trueOrFalse))
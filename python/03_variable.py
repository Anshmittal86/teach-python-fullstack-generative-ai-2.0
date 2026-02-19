# Variable:- Variable is like a container which can store a value so that we can use later in the code.

name = input("Enter your name: ")
print("Your name is " + name)


# Your name is ----- and you order ----.
name = input("Enter your name: ")
food = input("Enter your order: ")
print("Your name is " + name + " and you order " + food + ".")
print(f"Your name is {name} and you order {food}.")


# Task:- Take name and age from the user and print it.
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Your name is {name} and you are {age} year old.")

# Multiple Assignment
# a = 1
# b = 2
# c = 3
a, b, c = 1, 2, 3

# Same Value to multiple Variable
a = b = c = 1

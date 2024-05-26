# defines a function print_two with argument named *args which  allows for any number of arguments, 
def print_two(*args):
    arg1,arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# This function accepts a variable number of arguments and then unpacks them into arg1 and arg2. It prints these arguments.
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1} , arg2: {arg2}")

#this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this one takes no arguments
def print_none():
    print("I got nothin'.")

# prints the functions
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
    
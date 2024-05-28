# first called a function add with two arguments a and b , then add the two arguments to return the sum.
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

#defines a function subtract and assigns arguments a and b and calculate the difference and returns its difference.
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b
# defines a function multiply and assigns arguments a and b and calculate the product and returns its product.
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b} ")
    return a * b

# defines a function divide and assigns arguments a and b and divides and returns its value.
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

# These lines perform  arithemetic operations to calculate weight,height,age and iq
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight} , IQ: {iq}")

print("Here is a puzzle.")

# first we divide iq by 2 and then multiply weight by result division then subtract the result of the multiplication from height ,finally adds the age to the result of the subtraction to get result of what variable.
what = add(age, subtract(height, multiply(weight, divide(iq,2))))
print("That becomes: ",what, "Can you do it by hand?")

#initializing i as 0
i = 0
# numbers is an empty list that will store the values of i.
numbers = []

# The  while loop will continue to run until  i is less than 6.
while i < 6:
    print(f"At the top i is {i}")
    # The current value of i is appended to the numbers list.
    numbers.append(i)

# i is incremented by 1.
    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

# This iterates through the numbers list and prints each number
for num in numbers:
    print(num)
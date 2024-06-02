ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in that list. Let's fix that.")

# Split the string into a list of items
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
                 "Corn", "Banana", "Girl", "Boy"]

# Loop until 'stuff' contains exactly 10 items
while len(stuff) != 10:
# Remove and get the last item from 'more_stuff'
    next_one = more_stuff.pop()
    print("Adding: ", next_one)

# Append the item to 'stuff'
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")
print(stuff[1]) # Print the second item in the list (index 1)
print(stuff[-1])  # Print the last item in the list (index -1)
print(stuff.pop()) # Remove and print the last item in the list
print(' '.join(stuff)) # Join all items in the list into a single string separated by spaces
print('#'.join(stuff[3:5])) # Join the fourth and fifth items with a '#' in between
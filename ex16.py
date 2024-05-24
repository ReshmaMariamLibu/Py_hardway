# imports the argv variable from the sys module. 
from sys import argv

# this accepts two command line arguments script and filename and this values are unpacked from argv list.
script, filename = argv

# This lines gives information about actions to be performed in the specified file and prompt them to confirm or cancel the action by typing RETURN or CTRL-C.
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
input("?")

# This line truncates the content of the file. 
print("Opening the file...")
target = open(filename, 'w')

# It .truncates method truncates the content of the file.
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

# These lines tells to input the lines
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")

#These lines writes the lines and \n helps to move to the new line.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# this line closes the file, saving any changes made to it.
print("And finally, we close it.")
target.close()




# imports the argv variable from the sys module
from sys import argv

# this accepts two command line arguments script and filename and this values are unpacked from argv list.
script, input_file = argv

# This function takes a file object f as an argument and prints its entire content using the read() method.
def print_all(f):
    print(f.read())

# This function also takes a file object f as an argument and resets the file's current position to the beginning using the seek(0) method.
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

# opens the file specified by input_file and assigns the file object to current_file
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

#  rewind is used to reset the file's current position to the beginning.
rewind(current_file)

print("Let's print three lines:")

#Assigns current line to 1  
current_line = 1
print_a_line(current_line, current_file)

# increments the current line by 1
current_line = current_line + 1
print_a_line(current_line, current_file)

# increments the current line by 1
current_line = current_line + 1
print_a_line(current_line, current_file)
# imports the argv variable from the sys module. 
from sys import argv 

# this accepts two command line arguments script and filename and this values are unpacked from argv list.
script, filename =argv 

# This line opens the file specified by the filename variable in read mode and assigns the file object to the txt variable
txt = open(filename) 

# These lines print a message indicating the filename and then read the content of the file using the read() method of the file object txt. The content of the file is then printed.
print(f"Here's your file {filename}:") 
print(txt.read())

# This line prompts the user to enter the filename again. The filename is read using the input() function and stored in the variable file_again.
print("Type the filename again:")
file_again = input("> ")

# opens the file in read mode and assigns this on the txt_again variable
txt_again = open(file_again)

# finally prints it reads the file in read mode and prints in in the console.
print(txt_again.read())

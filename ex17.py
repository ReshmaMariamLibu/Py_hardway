# imports the argv variable from the sys module. 
from sys import argv

#Imports the exists function from the os.path module to check if a file exists.
from os.path import exists

## this accepts two command line arguments script from_file,to_file and this values are unpacked from argv list.
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#This line opens the file specified by the filename variable in read mode and assigns the file object to the in_file variable
in_file = open(from_file)
indata = in_file.read()

#calculates the length of the file in bytes.
print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue,CTRL-C to abort.")
input()

#This line opens the file specified by the filename variable in write mode and assigns the file object to the to_file variable
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright,all done.")

# this line closes the file, saving any changes made to it.
out_file.close()
in_file.close()


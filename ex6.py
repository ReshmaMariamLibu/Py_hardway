types_of_people = 10 # types_of_people value is assigned to 10
x = f"There are {types_of_people} types of people." # creates a string x using an f-string, which takes the value of the variable types_of_people into the string.

binary = "binary"
do_not = "don't"
y=f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: {y}")

hilarious = False # hilarious is set to false
joke_evaluation = "Isn't that joke so funny?! {}" # creates a string joke_evaluation with a placeholder {}
print(joke_evaluation.format(hilarious))

w = "This is the left side of...."
e = "a string with a right side."

print(w + e) # this line add the strings w and e together and prints the output.
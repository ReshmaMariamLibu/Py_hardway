formatter = "{} {} {} {}" #creates four placeholders

#This line substitutes the numbers 1, 2, 3, and 4 into the placeholders of the formatter string template using the format() method and then print it out.
print(formatter.format(1,2,3,4)) 

#This line substitutes the numbers one, two, three, and four into the placeholders of the formatter string template using the format() method and then prints the result.
print(formatter.format("one","two","three","four")) 

#same as above codes by substituting it using boolean values true and false and prints the output
print(formatter.format("True","False","False","True")) 

print(formatter.format(formatter,formatter,formatter,formatter))  #substitutes the formatter string template itself into each placeholder of the formatter string template and then prints the result.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
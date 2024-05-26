# This block defines a function named cheese_and_crackers which takes two parameters cheese_count and boxes_of_crackers. Inside the function, it prints  four lines of text that include the values of these parameters.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# two variables, amount_of_cheese and amount_of_crackers, are defined and assigned values. These variables are then passed as arguments to the cheese_and_crackers function
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# here cheese_and_crackers is assigned with values of amounts of cheese and crackers
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

# does math inside the function call
print("We can even do math inside too:")
cheese_and_crackers(10+20,5+6)

# This line combines variables and math in the function call. It adds 100 to the amount_of_cheese variable (10) and adds 1000 to the amount_of_crackers variable (50).
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

    
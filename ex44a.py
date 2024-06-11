# Define a Parent class with a method called implicit.
class Parent(object):

    def implicit(self):
        print("PARENT implicit()")


# Define a Child class that inherits from Parent.
class Child(Parent):
    pass

dad = Parent()

# Create an instance of Child called son.
son = Child()

dad.implicit()
# Call the implicit method on the Parent instance
son.implicit()
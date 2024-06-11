# Define a Parent class with a method called altered.
class Parent(object):

    def altered(self):
        print("PARENT altered()")

# Define a Child class that inherits from Parent and overrides the altered method.
class Child(Parent):
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD,AFTER PARENT altered()")

# Create an instance of Parent called dad.
dad = Parent()
# Create an instance of Child called son.
son = Child()

# Call the altered method on the Parent instance
dad.altered()
# Call the altered method on the Child instance
son.altered()

    
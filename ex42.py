# define a base class for animals.
class Animal(object):
    pass

# define a Dog class that inherits from Animal and initializes with a name attribute.
class Dog(Animal):
    def __init__(self, name):
        self.name = name

# define a Cat class that inherits from Animal and initializes with a name attribute.
class Cat(Animal):
    def __init__(self, name):
        self.name = name

# define a Person class with a name attribute and a pet attribute.
class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None

# define an Employee class that inherits from Person and adds a salary attribute.
class Employee(Person):
    def __init__(self, name, salary):
        # Call the constructor of the Person class.
        super(Employee, self).__init__(name)
        self.salary = salary

# define a base class for fish.
class Fish(object):
    pass

# define a Salmon class that inherits from Fish.
class Salmon(Fish):
    pass

# define a Halibut class that inherits from Fish.
class Halibut(Fish):
    pass

# Create an instance of Dog named "Rover".
rover = Dog("Rover")

# create an instance of Cat named "Satan".
satan = Cat("Satan")

# create an instance of Person named "Mary".
mary = Person("Mary")

# Set Mary's pet to the Cat instance named "Satan".
mary.pet = satan

# Create an instance of Employee named "Frank" with a salary of 120000.
frank = Employee("frank", 120000)

# Set Frank's pet to the Dog instance named "rover".
frank.pet = rover

# Create an instance of Fish.
flipper = Fish()

# Create an instance of Salmon.
crouse = Salmon()

# Create an instance of Halibut.
harry = Halibut()


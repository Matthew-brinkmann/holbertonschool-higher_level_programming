#!/usr/bin/python3
class Person:
    # The init methon runs as soon as an object of a class is instantiated.
    # Usefull to initialise and initial valuse in the object
    #still need to add "self" into the class even though the function takes no parameters.
    def __init__(self, name):
        # the name passed is set to the object (self.name) where name is the local varaible
        # that is specific to the __init__ method
        self.name = name


    def say_hi(self):
        print(f"Hello, how are you {self.name}?")


#the name 'Matthew' is sent through when setting p to the class person.
p = Person('Matthew')
p.say_hi()
# The previous 2 lines can also be written as
# Person().say_hi()

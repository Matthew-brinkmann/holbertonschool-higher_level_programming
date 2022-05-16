#!/usr/bin/python3
class Robot:
    #used to store and create robots with names
    # Population is a variable used to count total number of Robots
    # it is a class variable, so anything with class
    # Robot can edit this variable though syntax
    # class.variable
    population = 0

    def __init__(self, name):
        self.name = name
        print(f"(Creating {self.name})")
        # After robot is created, we add 1 to 'population'
        Robot.population += 1


    def die(self):
        # removes 1 from population
        Robot.population -= 1

        if Robot.population == 0:
            print(f"{self.name} was the last robot.")
        else:
            print(f"there are still {Robot.population} robats alive.")


    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")


    # how_many is a class method, meaning it belongs to the whole class
    # NOT to this object (instance of the class).
    @classmethod
    def how_many(cls):
        # Prints population
        print(f"there are {cls.population} robots.")


robot1 = Robot("R2-D2")
robot1.say_hi()
Robot.how_many()

robot2 = Robot("c-3P0")
robot2.say_hi()
Robot.how_many()

print("\nTobots can do some work here \n")

print("Robots have finished their work, we can decomission them now")
robot1.die()
robot2.die()

Robot.how_many()

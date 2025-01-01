

############################################################################################################
############################################################################################################
#################################### Climbing Game -- Fun Project ##########################################
############################################################################################################
############################################################################################################

import unittest
import random
from time import sleep

try_example = """
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result is {result}")
except Exception as e:  # Catch any exception and get its details
    print(f"An error occurred: {e}")
"""

# -------------------------------------------------------------------------------------------------------- #
# Person Class (Player Setup)
# -------------------------------------------------------------------------------------------------------- #

class Person:

    def __init__(self, name, style):
        self.name = name
        self.style = style

    def __str__(self):
        return f"{self.name} : {self.style}"

# -------------------------------------------------------------------------------------------------------- #
# Stats Class (Generating Stats for Person)
# -------------------------------------------------------------------------------------------------------- #

class Stats:

    def __init__(self):
        self.str = random.randint(1, 11)
        self.pow = random.randint(1, 11)
        self.end = random.randint(1, 11)
        self.powend = random.randint(1, 11)

    def __str__(self):
        return (
            "Stats:\n"
            f"  Strength: {self.str}\n"
            f"  Power: {self.pow}\n"
            f"  Endurance: {self.end}\n"
            f"  Power Endurance: {self.powend}"
            )

# -------------------------------------------------------------------------------------------------------- #
# Rock Climbs (Making the Climbs)
# -------------------------------------------------------------------------------------------------------- #


## Needed help with this; still learning how to properly have classes interact with each other. Lots of 'self.' stuff
## New item learned:
    ## The super() function is used in a child class to call a method from the parent class.
    ## This ensures that the parent class's initialization or behavior is preserved.


class Climb:

    def __init__(self, base_diff, multiplier):
        self.base_diff = random.randint(1, base_diff)
        self.multiplier = multiplier
        self.difficulty = self.base_diff * self.multiplier

class v_Hero(Climb): ## Easy climb - respectfully

    def __init__(self):
        super().__init__(multiplier=0.2, base_diff=20)  

    def __str__(self):
        return f"{self.difficulty}"

class more_diff_climbs:
    pass


# -------------------------------------------------------------------------------------------------------- #
# Climbing Management (Managing everything)
# -------------------------------------------------------------------------------------------------------- #

class Climbing_Game:

    def __init__(self):
        self.person = None
        self.stats = None

    def create_person(self):
        name = input("Name: ")
        style = input("Style: ")
        self.person = Person(name, style)
        print(self.person)

    def create_stats(self):
        self.stats = Stats()
        print(self.stats)
       
        
    def run(self):
        self.create_person()
        self.create_stats()
        
        


# -------------------------------------------------------------------------------------------------------- #
# Running the game
# -------------------------------------------------------------------------------------------------------- #

if __name__ == '__main__':

    try:
        game = Climbing_Game()
        game.run()
        
    except Exception as e:  # Catch any exception and get its details
        print(f"An error occurred: {e}")
        
# -------------------------------------------------------------------------------------------------------- #
# Git commands
# -------------------------------------------------------------------------------------------------------- #
 
## Make sure to:
# git init
# git add .
# git commit -m " - notes - "
# git push

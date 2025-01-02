

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

    def stats_distribution(self):
        stats = self.str, self.pow, self.end, self.powend
        return stats
        

# -------------------------------------------------------------------------------------------------------- #
# Rock Climbs (Making the Climbs)
# -------------------------------------------------------------------------------------------------------- #

#================================
# GPT'd
#================================
## Needed help with this; still learning how to properly have classes interact with each other. Lots of 'self.' stuff
## New item learned:
    ## The super() function is used in a child class to call a method from the parent class.
    ## This ensures that the parent class's initialization or behavior is preserved.
#================================

class Climb:

    def __init__(self, moves, base_diff, multiplier):
        self.base_diff = random.randint(1, base_diff)
        self.multiplier = multiplier
        self.moves = random.randint(2, moves)
        self.difficulty = self.base_diff * self.multiplier

class v_Hero(Climb): ## Easy climb - respectfully

    def __init__(self):
        super().__init__(moves=8, multiplier=0.2, base_diff=20)  

    def __str__(self):
        return f"This is v_Hero, difficulty at {self.difficulty} with {self.moves} moves."

class more_diff_climbs:
    pass


# -------------------------------------------------------------------------------------------------------- #
# Climbing Management (Managing everything)
# -------------------------------------------------------------------------------------------------------- #

#================================
# GPT'd
#================================
class Climbing:
    def __init__(self, climb, stats):
        self.climb = climb  # Instance of a climb, e.g., v_Hero
        self.stats = stats  # Instance of climber stats, e.g., Stats()

    def attempt_climb(self):
        print(f"Starting climb: {self.climb}")
        for i in range(1, self.climb.moves + 1):
            move_difficulty = random.uniform(1, self.climb.difficulty)  # Random difficulty for each move
            climber_stat = random.choice(self.stats.stats_distribution())  # Randomly select one stat

            print(f"\nMove {i}:")
            print(f"  Move Difficulty: {move_difficulty:.2f}")
            print(f"  Climber Stat: {climber_stat}")

            if climber_stat >= move_difficulty:
                print("You succeeded on this move!")
            else:
                print("You failed this move! Game over.")
                return False  # Climber failed
        print("Congratulations! You completed the climb!")
        return True  # Climber succeeded
#================================

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

        #================================
        # GPT'd
        #================================
        # Step 1: Create player and stats
        self.create_person()
        self.create_stats()

        # Step 2: Create a climb
        climb = v_Hero()  # Example climb

        # Step 3: Attempt the climb
        climbing = Climbing(climb, self.stats)
        success = climbing.attempt_climb()

        # Step 4: Game result
        if success:
            print(f"{self.person.name} successfully completed the climb!")
        else:
            print(f"{self.person.name} failed the climb. Better luck next time!")
        #================================

        

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

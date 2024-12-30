

############################################################################################################
############################################################################################################
#################################### Climbing Game -- Fun Project ##########################################
############################################################################################################
############################################################################################################


## Absolutly butchered second attempt --- GPT helped me organize. 

import random
from time import sleep

# -------------------------------------------------------------------------------------------------------- #
# Person Class (Player Setup)
# -------------------------------------------------------------------------------------------------------- #

class Person:
    person_count = 0  # Tracks the number of players

    def __init__(self, name):
        Person.person_count += 1
        self.id = Person.person_count
        self.name = name

    def __str__(self):
        return f"{self.name:<15}"

    def print_greeting(self):
        print(f"Hello, {self.name}! You're climber #{self.id} today. Let's build your profile.")

# -------------------------------------------------------------------------------------------------------- #
# Climber Class (Stats Setup)
# -------------------------------------------------------------------------------------------------------- #

class Climber:
    def __init__(self):
        self.str = random.randint(1, 11)
        self.pow = random.randint(1, 11)
        self.end = random.randint(1, 11)
        self.powend = random.randint(1, 11)

    def __str__(self):
        return (
            f"Stats:\n"
            f"  Strength - {self.str}\n"
            f"  Power - {self.pow}\n"
            f"  Endurance - {self.end}\n"
            f"  Power Endurance - {self.powend}"
        )

# -------------------------------------------------------------------------------------------------------- #
# Climb Base Class
# -------------------------------------------------------------------------------------------------------- #

class Climb:
    def __init__(self, difficulty_multiplier, base_difficulty):
        self.difficulty_multiplier = difficulty_multiplier
        self.base_difficulty = base_difficulty

    def difficulty(self):
        return random.randint(1, self.base_difficulty) * self.difficulty_multiplier

    def climber_stats(self, climber):
        climber_stats = [climber.str, climber.end, climber.end, climber.powend]
        return random.choice(climber_stats)

    def climb(self, climber):
        moves = random.randint(1, 8)
        print(f"\nThis climb has {moves} moves.")
        for move in range(1, moves + 1):
            move_difficulty = self.difficulty()
            climber_stat = self.climber_stats(climber)

            print(f"\nMove {move}:")
            print(f"  Move Difficulty: {move_difficulty:.2f}")
            print(f"  Climber's Stat: {climber_stat}")

            if climber_stat < move_difficulty:
                print("\nYou fell and Died! Game over. 😢")
                return

            choice = input("Do you want to make the next move? (yes/no): ").strip().lower()
            if choice != "yes":
                print("You chose not to move. Ending climb.")
                return

        print("\nCongratulations! You completed the climb! 🧗‍♂️")

# -------------------------------------------------------------------------------------------------------- #
# Specific Climbs (Derived Classes)
# -------------------------------------------------------------------------------------------------------- #

class VHero(Climb):
    def __init__(self):
        super().__init__(difficulty_multiplier=0.2, base_difficulty=30)

    def __str__(self):
        return "VHero: A medium-difficulty climb."

class SlurpinOnCreams(Climb):
    def __init__(self):
        super().__init__(difficulty_multiplier=0.2, base_difficulty=40)

    def __str__(self):
        return "Slurpin On Creams: A mega-hard climb."

# -------------------------------------------------------------------------------------------------------- #
# Game Manager
# -------------------------------------------------------------------------------------------------------- #

class ClimbingGame:
    def __init__(self):
        self.player = None
        self.climber = None

    def create_person(self):
        name = input("Enter your climber's name: ").strip()
        self.player = Person(name)
        self.player.print_greeting()

    def create_climber(self):
        print("\nGenerating your climber's stats...")
        sleep(1)
        self.climber = Climber()
        print(self.climber)

    def choose_climb(self):
        print("\nChoose your climb:")
        print("  1. VHero (Medium difficulty)")
        print("  2. Slurpin On Creams (Hard difficulty)")

        choice = input("Enter 1 or 2: ").strip()
        if choice == "1":
            return VHero()
        elif choice == "2":
            return SlurpinOnCreams()
        else:
            print("Invalid choice. Try again.")
            return self.choose_climb()

    def start_climb(self):
        climb = self.choose_climb()
        print(f"\nYou've chosen: {climb}")
        climb.climb(self.climber)

    def run(self):
        self.create_person()
        self.create_climber()
        while True:
            self.start_climb()
            play_again = input("\nDo you want to try another climb? (yes/no): ").strip().lower()
            if play_again != "yes":
                print("Thanks for playing! Goodbye! 👋")
                break

# -------------------------------------------------------------------------------------------------------- #
# Run the Game
# -------------------------------------------------------------------------------------------------------- #

if __name__ == "__main__":
    game = ClimbingGame()
    game.run()

# -------------------------------------------------------------------------------------------------------- #

## Git commands
 
## Make sure to:
# git init
# git add .
# git commit -m " - notes - "
# git push

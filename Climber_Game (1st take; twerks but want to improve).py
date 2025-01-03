

## Climbing Game -- Fun Project


# --------------------------------------------------------------------------- #

## Imports

import random

# --------------------------------------------------------------------------- #


##  Classes

class Climber:

    climberCount = 0

    def __init__(self, name, style, str, pow, end, powend, health = 100):

        # ==== work in progress
        print(f"New CLIMBER")
        Climber.climberCount += 1
        # ====

        self.name = name
        self.style = style
        self.str = str
        self.pow = pow
        self.end = end
        self.powend = powend

    def __str__(self):
        return f"{self.name}: style {self.style}"

    def __repr__(self):
        return f"New climber {self.name}, {self.style}, stats: Str{self.str}; Pow{self.pow}; End{self.end}; PowEnd{self.powend}" ## Better update needed

    def header():
        pass
    
    ## Ideas
    
    def died(self):
        pass

class open_for_grabs:
    pass   

class Rock_Climb:

    def __init__(self, name, difficulty = 20):
        self.name = name
        self.difficulty = difficulty

    def __repr__(self):
        return f"{self.name}"

    # ========> GPT'd for help; this was a challenge... I was kind of on track though. 
    def climbing_climb(self, climber):
        # Calculating number of moves in climb
        rand_move_num = random.randint(1, 8)
        print(f"Total moves: {rand_move_num}")

        for move in range(1, rand_move_num+1):
            # Calculating move difficulty
            rand_move_dif = (random.randint(1, self.difficulty) * .20) ## .20 = arbitrary; I wonder if this could be randomly generated ...  stat generation based on easy medium or hard mode.. but that is to much

            # Picking random climber stat
            climber_stats = climber.str, climber.end, climber.end, climber.powend
            rand_climber_stat = random.choice(climber_stats)

            # Display move details
            print(f"\nMove {move}:")
            #print(f"  Move difficulty: {rand_move_dif:.2f}")  ## nice to have but don't want to see difficulty
            print(f"  Chosen climber stat: {rand_climber_stat}")

            # Check if the climber can make the move
            if rand_climber_stat < rand_move_dif:
                print("You fell and died!")
                return  # Exit the climb

            # Ask climber if they want to make the move
            choice = input("Do you want to make the move? (yes/no): ").lower()
            if choice != "yes":
                print("You chose not to move. Ending climb.")
                return

        # If all moves are successfully made
        print("\nCongratulations! You completed the climb!‍️")
    # ========>


class open_for_grabs:
    pass

# --------------------------------------------------------------------------- #

# Climber profiles  --- lower stats makes it hard -- raising stats makes game easier.. 

## Dummy climber
dumRico = Climber("Enrico", "balls-limic", 7, 7, 9, 8)

#Strength climber
dumJesse = Climber("Jesse", "OTC", 10, 8, 4, 7) #total 29

# Power climber
dumMagnus = Climber("Magnus", "Campus Everything", 7, 9, 5, 8) #total 

# Enduro climber
dumGruper = Climber("Jesse Gruper", "No power, never tired", 5, 5, 10, 7) #total 

# Power Enduro climber
dumMegos = Climber("Megos", "So German", 7, 7, 5, 10) #total

# --------------------------------------------------------------------------- #

## Profiles for player to pick

Jesse = ("OTC", 10, 8, 4, 7)

Magnus = ("Campus Everything", 7, 9, 5, 8)

Gruper = ("No power, never tired", 5, 5, 10, 7)  ## no power, never tired is funny

Megos = ("So German", 7, 7, 5, 10)


# --------------------------------------------------------------------------- #

# Climbs to pick from --- or are in the gauntlet

## Test Rock Climb
v_zero = Rock_Climb("Testy")

## A harder Rock Climb
segatron = Rock_Climb("Segatron", 30)

## Slab is for Kings
dandie_smearon = Rock_Climb("Dandie Smearon", 40)  ## 40 is the highest number

## Slurpin Some Cream
slurpin_some_creams = Rock_Climb("Slurpin Some Creams", 50) ## No, 50 is.. ppl will die in this game

## NOTES: How can I set these up -- to contain specific requirements.. (maybe to difficult for me atm).. Lets just climb for now.. 

# --------------------------------------------------------------------------- #

## Getting player data
               
entry_climber = input("Welcome to the climbing gulag! You'll be tested against the best! Enter your name: ")
                
choice = input(f"Okay, {entry_climber}. What is your profile: a) Strength; b) Power; c) Endurance; d) Power Endurance. Which one -> a, b, c, or d?")
while choice != 'a' and choice != 'b' and choice != 'c' and choice != 'd':
  choice = input("Whoops, it looks like you didn't choose a, b, c, or d. Try selecting again!")

tot_stats = [] ## this captures a tuple in a list format ....  captured in stats below via stats[0]..

if choice == "a":
    tot_stats.append(Jesse)
elif choice == "b":
    tot_stats.append(Magnus)
elif choice == "c":
    tot_stats.append(Gruper)
elif choice == "d":
    tot_stats.append(Megos)

stats = tot_stats[0] ## messed up .... maybe can stream line this..

player_one = Climber(entry_climber, stats[0], stats[1], stats[2], stats[3], stats[4])  ## Need to change the name of this
print(player_one)
    
# --------------------------------------------------------------------------- #

# Playing the Game

play_the_game = input("Your stats are set.. Attemp a climb? (Yes or No)")

#Picking a climb (v_zero; segatron; dandie_smearon)

if play_the_game == "No":
    print("Byeeee!")
    
if play_the_game == "Yes":                          ## I don't know how to exit if a climber dies

    print("You'll first climb 'Testy', the easiest climb.")
    v_zero.climbing_climb(player_one)

    
holding = '''

    print("Now you're climbing 'Segatron'")
    segatron.climbing_climb(player_one)

    print("You're climbing 'Dandie Smearon'")
    dandie_smearon.climbing_climb(player_one)

    print("Now you're climbing 'Slurpin Some Creams'")
    slurpin_some_creams.climbing_climb(player_one)
    '''


# --------------------------------------------------------------------------- #

## Git commands
 
## Make sure to:
# git init
# git add .
# git commit -m " - notes - "
# git push

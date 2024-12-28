## Game!

## Climbing Game -- Fun Project
## One player type of game, kind of exploring projects..
## If a move fails, the climber dies
## There is a climber, a project with moves
## takes climbers levels (endurace, pwoer, sterngth, and PE)
## Climber is tested on the climbs requirments


#### Thoughts:
    ## I am wondering how to create a climb with a randomly rolled difficulty
    ## then match it up to the climber
    ## That will be the bases of the game!
    ## I don't know how to store climbers and climbs.. 

# --------------------------------------------------------------------------- #

## Imports

import random

# --------------------------------------------------------------------------- #


##  Classes


class Climber:

    def __init__(self, name, style, str, pow, end, powend, health = 100): 
        self.name = name
        self.style = style
        self.str = str
        self.pow = pow
        self.end = end
        self.powend = powend

    def __repr__(self):
        return f"New climber {self.name}, {self.style}, stats: Str{self.str}; Pow{self.pow}; End{self.end}; PowEnd{self.powend}" ## Better update needed

    ## Ideas
    
    def climb_attempt(self):
        pass

    def lose_health(self):
        pass

    def died(self):
        pass
    

class Rock_Climb:

    def __init__(self, name, difficulty = 20):
        self.name = name
        self.difficulty = difficulty

    def __repr__(self):
        return f"{self.name}"

    ## Maybe climbs can be built were certain stats are required to make moves.. 

    ## Will add more stuff

    ## Working with ideas
        # Trying to create climbs requirements based on stats
        # if climber attempts without meet requirements, they die.. 

    def start_climb(self, climber):

        ## Requires 8 strength to complete..
        ## WIll only do this one to see how easy it works (or not)..

        requirement = self.difficulty * .25 ## A stat needs to be 25% of diff. (arbitrary)   
    
        while True:
            if climber.str < requirement:
                print("Not Strong enough")
                break
            elif climber.pow < requirement:
                print("Now Powerful enough")
                break
            elif climber.end < requirement:
                print("Now Enduro enough")
                break
            elif climber.powend < requirement:
                print("Now Power Enduro enough")
                break
            else:
                print("Send it!")
                break

    ## Ideas
    def climbing_climb(self, climber):

        ## The idea here is to create a random roll some how
        ## the climber gets to choose where or not they want to make a move..
        ## If a roll is higher than a stat, or stat combo then climber falls and dies
        ## if stats are higher than roll, then climber continues..
        ## how can I create a total number of movers per climb then and create the random roll difficulty measure for climbers to beat..

        ## It would be something like...

        # Calculating move difficulty
        rand_move_dif = (random.randint(1, self.difficulty) * .20)   ## Pick .20 arbitrarily -- subject to change

        # Calculating number of moves in climb
        rand_move_num = random.randint(1, 8)

        # Picking random climber stat
        climber_stats = climber.str, climber.end, climber.end, climber.powend
        rand_climber_stat = random.choice(climber_stats)

        ## Climbing

        


# =========>>>  DAVID
## If you'd like, create a random class that interacts with stuff..
class David:
    pass


# --------------------------------------------------------------------------- #


## Game Intro

# Saving these for later -- > climber profiles

## Dummy climber
Rico = Climber("Enrico", "balls-limic", 7, 7, 9, 8)

#Strength climber
Jesse = Climber("Jesse", "OTC", 10, 8, 4, 7) #total 29

# Power climber
Magnus = Climber("Magnus", "Campus Everything", 7, 9, 5, 8) #total 

# Enduro climber
Gruper = Climber("Jesse Gruper", "No power, never tired", 5, 5, 10, 7) #total 

# Power Enduro climber
Megos = Climber("Megos", "So German", 7, 7, 5, 10) #total

# --------------------------------------------------------------------------- #

## Based off Davids Idea || Profiles based off them

Jesse = ("OTC", 10, 8, 4, 7)

Magnus = ("Campus Everything", 7, 9, 5, 8)

Gruper = ("No power, never tired", 5, 5, 10, 7)

Megos = ("So German", 7, 7, 5, 10)


# --------------------------------------------------------------------------- #

# Climbs to use

## Test Rock Climb
v_zero = Rock_Climb("Testy")

## A harder Rock Climb
segatron = Rock_Climb("Segatron", 30)

## Slab is for Kings
dandie_smearon = Rock_Climb("Dandie Smearon", 40)  ## 40 is the highest number

## NOTES: How can I set these up -- to contain specific requirements.. (maybe to difficult for me atm).. Lets just climb for now.. 

# --------------------------------------------------------------------------- #
               
entry_climber = input("Welcome to the climbing gulag! You'll be tested against the best! Enter your name: ")

#>>>>>>>  Idea
## May have a create your own
#climber_style = input("Describe your climbing style in one word: ")
#>>>>>>>

                
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

entry_climber

stats = tot_stats[0] ## messed up .... maybe can stream line this..



player_one = Climber(entry_climber, stats[0], stats[1], stats[2], stats[3], stats[4])  ## Need to change the name of this
print(player_one)
    
# --------------------------------------------------------------------------- #

## Testing
      

#print(rico)
#print(rico.str)


#print(v_zero)
#print(v_zero.difficulty)

## Test Climber on Climb -- if stats don't sum up to/ greater than difficulty .. climber falls and dies

## Have to figure out how to automatically pull each stat. 
def attempting_climb(climber, climb):
    total_stats = climber.str + climber.pow + climber.end + climber.powend
    # return total_stats
    if total_stats >= climb.difficulty:
        print(f"{climber} successfully climb {climb}, and didn't die")
    else:
        print(f"{climber} died climbing {climb}")


# attempting_climb(Rico, v_zero) # testing function

# --------------------------------------------------------------------------- #

## 

#Starting
play_the_game = input("Your stats are set.. Attemp a climb? (Yes or No)")

#Picking a climb (v_zero; segatron; dandie_smearon)

if play_the_game == "No":
    print("Byeeee!")
elif play_the_game == "Yes":
    print("Nice, now pick a climb!")

climb = []

# =======> Needs work

while play_the_game == "Yes":
    picking_climb = input("What climb? 1) v_zero; 2) segatron; or 3) dandie_smearon. Type in 1, 2, or 3")
    if picking_climb == "v_zero":
        climb.append(v_zero)
    elif picking_climb == "segatron":
        climb.append(segatron)
    elif picking_climb == "dandie_smearon":
        climb.append(dandie_smearon)
        
# =======>
    

# --------------------------------------------------------------------------- #

## Playing the game
play_the_game


# --------------------------------------------------------------------------- #

## Git commands
 
## Make sure to:
# git init
# git add .
# git commit -m " - notes - "
# git push

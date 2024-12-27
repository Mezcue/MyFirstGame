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

##  Classes
 
class Climber:

    def __init__(self, name, style, str, pow, end, powend):
        self.name = name
        self.style = style
        self.str = str
        self.pow = pow
        self.end = end
        self.powend = powend

    def __repr__(self):
        return f"New climber {self.name}, {self.style}, stats: Str{self.str}; Pow{self.pow}; End{self.end}; PowEnd{self.powend}" ## Better update needed

    ## Will add more stuff

class Rock_Climb:

    def __init__(self, name, difficulty = 20):
        self.name = name
        self.difficulty = difficulty

    def __repr__(self):
        return f"{self.name}"

    ## Maybe climbs can be built were certain stats are required to make moves.. 

    ## Will add more stuff
# --------------------------------------------------------------------------- #

## Testing
      
## Test Climber
rico = Climber("Enrico", "balls-limic", 7, 7, 9, 8)
#print(rico)
#print(rico.str)

## Test Rock_Climb
v_zero = Rock_Climb("Testy")
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


attempting_climb(rico, v_zero) # testing function

# --------------------------------------------------------------------------- #

## Game Intro

# climber profiles
# strenght, power, endurance, power endurance

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

total_package = Climber(entry_climber, stats[0], stats[1], stats[2], stats[3], stats[4])
print(total_package)
    
# --------------------------------------------------------------------------- #

## Git commands
 
## Make sure to:
# git init
# git add .
# git commit -m " - notes - "
# git push
